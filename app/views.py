# python modules
import os
import csv

# 3rd party 
from rest_framework.decorators import api_view, parser_classes
from rest_framework.utils.serializer_helpers import ReturnList, ReturnDict
from rest_framework import parsers, exceptions, serializers, response
# import pandas

# my modules
from app.serializers import TempFileSerializer
from app.models import TempFile, Data

cwd = os.getcwd()
print(cwd)

# Create your views here.
parser_classes([parsers.FileUploadParser])
@api_view(["POST"])
def csv_file_api(request):
    try:
        serialized_file = TempFileSerializer(data=request.data)
        if serialized_file.is_valid():
            file = serialized_file.save()
            path = cwd + str(file.file.url).replace("/", os.sep)
            with open(path, "r") as f:
                csv_dict_reader = csv.DictReader(f, ["id", "state", "other"])
                for  row in csv_dict_reader:
                    try:
                        pk = int(row.pop("id"))
                        print(row)
                        Data.objects.filter(pk=pk).update(**row)
                    except Exception as e:
                        print(e)
            '''
            df = pandas.read_csv(path)
            for i in df.index:
                try:
                    data = Data.objects.get(pk=int(df["id"][i]))
                    data.state = df["state"][i]
                    data.save()
                    print("updated")
                except Exception as e:
                    # print(e)
                    raise e
            '''
            os.remove(path)
            file.delete()
            return response.Response(ReturnDict({"msg": "Success"}, serializer=serializers.Serializer), status=200)
        raise Exception("Invalid data recieved!")
    except Exception as e:
        return response.Response(ReturnDict({"error": str(e)}, serializer=serializers.Serializer), status=400)
from rest_framework.serializers import ModelSerializer
from app import models

class TempFileSerializer(ModelSerializer):
    class Meta:
        model = models.TempFile
        fields = "__all__"
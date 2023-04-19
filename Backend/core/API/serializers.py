# myapi/serializers.py
from rest_framework import serializers
# from .models import Result,File
from .models import File


# class ResultSerializers(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Result
#         fields = ('speaker','transcript')

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('__all__')


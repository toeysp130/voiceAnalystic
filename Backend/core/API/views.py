# views.py
from rest_framework import viewsets
# from .serializers import ResultSerializers,FileSerializer
from .serializers import FileSerializer

# from .models import Result,File
from .models import File



# class ResultViewSet(viewsets.ModelViewSet):
#     queryset = Result.objects.all()
#     serializer_class = ResultSerializers

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all().order_by('-uploaded_at')
    serializer_class = FileSerializer

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema

from .models import *
from .serializers import *

# Create your views here.
class PerevalViewset(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    filterset_fields = ['user__email']

    # убираем нереализованные методы delete, put
    @swagger_auto_schema(auto_schema=None)
    def update(self, request, *args, **kwargs):
        pass

    @swagger_auto_schema(auto_schema=None)
    def destroy(self, request, *args, **kwargs):
        pass

    def create(self, request, *args, **kwargs):
        try:
            serializer = PerevalSerializer(data=request.data)
            if serializer.is_valid():
                instance = serializer.save()
                return Response({"status": 200, "message": "Успешно отправлено", "id": instance.id})
            else:
                return Response({"status": 400, "message": "Bad Request", "id": None})
        except Exception as no_connection_to_the_db:
            return Response({"status": 500, "message": "Ошибка подключения к базе данных", "id": None})

    def retrieve(self, request, *args, **kwargs):
        try:
            pereval = self.get_object()
            serializer = PerevalSerializer(pereval)
            return Response(data=serializer.data)
        except Http404:
            return Response({"state": 0, "message": "Запись с таким id не найдена"})

    def partial_update(self, request, *args, **kwargs):
        pereval = self.get_object()
        if pereval.status != 'NW':
            return Response({"state": 0, "message": "Можно редактировать записи только в статусе 'NW'"})
        else:
            serializer = PerevalSerializer(pereval, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'state': 1, 'message': 'Запись успешно изменена',})
            else:
                return Response({'state': 0, 'message': serializer.errors})






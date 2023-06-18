import random
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
# from .serializers import CargoCreateRetrieveSerializer, CarSerializer, CargoPatchSerializer, CargoListSerializer
from geopy.distance import geodesic
# from .models import Car, Cargo, Location
from .models import Campaign, Message, Client
from .serializers import CampaignSerializer, ClientSerializer, MessageSerializer
from rest_framework import views
from rest_framework import generics, mixins
from . import signals


class CampaignViewSet(mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    queryset = Campaign.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ["get", "delete", "post", ]
    serializer_class = CampaignSerializer

    def create(self, request, *args, **kwargs):
        print(request.data.get('text_message'))
        response = super().create(request, *args, **kwargs)
        # city = ["Москва", "Уфа", "Казань", "Пермь", "Краснодар", "Санкт-Петербург", "Новосибирск", "Екатеринбург",
        #         "Красноярск", "Челябинск"]
        # for i in range(600):
        #     Client.objects.create(phone_number=str(random.randint(79100000000, 79599999999)), tag=random.choice(city))


        # signals.user_signal.send(sender=None, instance=None, bordomvatic_id="bordomatic_id",
        #                          task_id="task_id")
        # print(response.data.get("id"))

        return response


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ["get", "delete"]
    serializer_class = MessageSerializer


class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ["get", "patch", "delete", "post", ]
    serializer_class = ClientSerializer

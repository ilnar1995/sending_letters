from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Mailing, Message, Client
from .serializers import MailingSerializer, ClientSerializer, MessageSerializer
from rest_framework import generics, mixins


class CampaignViewSet(mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    queryset = Mailing.objects.all()
    permission_classes = (AllowAny,)
    http_method_names = ["get", "delete", "post", ]
    serializer_class = MailingSerializer


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

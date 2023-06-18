import django
from django.urls import path, include
from django.contrib.auth import views

from rest_framework.routers import SimpleRouter


# from .views import CargoModelListUpdateViewSet, CarModelViewSet, CargoModelRetrieveCreateViewSet
from .views import CampaignViewSet, MessageViewSet, ClientViewSet

# ## cargo_router/
# cargo_router = SimpleRouter()
# cargo_router.register(r"cargo", CargoModelListUpdateViewSet)
## campaign_router/
campaign_router = SimpleRouter()
campaign_router.register(r"campaign", CampaignViewSet)
## car_router/
client_router = SimpleRouter()
client_router.register(r"client", ClientViewSet)
## car_router/
message_router = SimpleRouter()
message_router.register(r"message", MessageViewSet)
from .views import *

urlpatterns = [
    # # path("", include(cargo_router.urls)),
    # path("", include(car_router.urls)),
    path("", include(campaign_router.urls)),
    path("", include(client_router.urls)),
    path("", include(message_router.urls)),
    # path('get_cargos/', CargoModelListUpdateViewSet.as_view({'get': 'list'}), name='get_cargo'),
    # path('create_cargo/', CargoModelRetrieveCreateViewSet.as_view({'post': 'create'}), name='createcargo'),
    # path('update_cargo/<int:pk>/', CargoModelListUpdateViewSet.as_view({'patch': 'partial_update'}), name='update_cargo'),
    # path('get_cargo/<int:pk>/', CargoModelRetrieveCreateViewSet.as_view({'get': 'retrieve'}), name='retrieve_cargo'),
    # path('delete_cargo/<int:pk>/', CargoModelListUpdateViewSet.as_view({'delete': 'destroy'}), name='destroy_cargo'),
]

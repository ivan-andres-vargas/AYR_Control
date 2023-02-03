
from django.urls import path, include

from . import views
from .views import ClienteViewSet, RepresentanteLegalViewSet, FuncionarioContactoViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'representantes', RepresentanteLegalViewSet, basename='representante')
router.register(r'funcionarios', FuncionarioContactoViewSet, basename='funcionario')

urlpatterns = [
    path('', include(router.urls)),
]

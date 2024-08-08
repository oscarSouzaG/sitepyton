from django.urls import path
from . import views
from .views import registro_uso_veiculo
from .views import home

urlpatterns = [
    path('', views.home, name='home'),
    path('registro_veiculo/', views.registro_uso_veiculo, name='registro_veicular'),
    # Certifique-se de que o nome está correto
    # outras URLs

]
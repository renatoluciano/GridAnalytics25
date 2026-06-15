from django.urls import path
from . import views

urlpatterns = [
    # Rota raiz do app que chama a nossa view de dashboard
    path('', views.dashboard_f1, name='dashboard_f1'),
]

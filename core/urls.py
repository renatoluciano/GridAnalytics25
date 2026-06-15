from django.contrib import admin
from django.urls import path, include  # Certifique-se de importar o 'include'

urlpatterns = [
    path('admin/', admin.site.name),
    # Encaminha a página inicial do projeto diretamente para o nosso app
    path('', include('analisador.urls')), 
]

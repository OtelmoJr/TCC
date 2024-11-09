from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página inicial
    path('gerar_recomendacao/', views.gerar_recomendacao_view, name='gerar_recomendacao')
]


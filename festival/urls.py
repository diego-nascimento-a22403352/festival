from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('dias/', views.dias_view, name='dias'), # ROTA ADICIONADA
    path('palcos/', views.palcos_view, name='palcos'),
    path('concertos/<int:id>/', views.concerto_view, name='concerto'),
]
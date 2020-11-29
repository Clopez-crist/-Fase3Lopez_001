from django.urls import path
from catalogo import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('games/', views.GameListView.as_view(), name='games'),
    path('gamess/<int:pk>', views.GameDetailView.as_view(), name='game-detail'),
    path('categoria/', views.categoria, name='categoria'),
    path('mejorjuego/', views.mjrjuego, name='mjrjuego'),
    path('retrogames/', views.retrogame, name='retro'),
    path('formulario/', views.formulario, name='formulario'),
    path('register/', views.register, name='register'),
]


urlpatterns+= [
    path('game/create/', views.GameCreate.as_view(), name='game_create'),
    path('game/<int:pk>/update/', views.GameUpdate.as_view(), name='game_update'),
    path('game/<int:pk>/delete/', views.GameDelete.as_view(), name='game_delete'),

]
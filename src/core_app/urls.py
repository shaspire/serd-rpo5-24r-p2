from django.urls import path
from . import views

urlpatterns = [
    # Главная страница и категории
    path('', views.ad_list_view, name='ad_list'),
    path('category/<slug:slug>/', views.ad_list_view, name='category_list'),

    # CRUD объявлений и избранное
    path('ad/new/', views.ad_create_view, name='ad_create'),
    path('ad/<uuid:uuid>/', views.ad_detail_view, name='ad_detail'),
    path('ad/<uuid:uuid>/edit/', views.ad_update_view, name='ad_update'),
    path('ad/<uuid:uuid>/delete/', views.ad_delete_view, name='ad_delete'),
    path('ad/<uuid:uuid>/favorite/', views.toggle_favorite, name='toggle_favorite'),

    # Профиль пользователя
    path('accounts/profile/', views.profile_view, name='profile'),

    # Авторизация и регистрация
    path('accounts/register/', views.register_view, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
]
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("Tarif", views.genre, name="Tarif"),
    path("oneTarif/<int:dk>", views.oneTarif, name="oneTarif"),
    path("Client/new/", views.Client_new, name="Client_new"),
    path("Client/<int:kp>/edit/", views.Client_edit, name="Client_edit"),
    path("Client/<int:kp>/delete/", views.Client_delete, name="Client_delete"),
    path("Operator/", views.operator, name="operator"),
    path("Tarif/new/", views.Tarif_new, name="Tarif_new"),
    path("Tarif/<int:kp>/edit/", views.Tarif_edit, name="Tarif_edit"),
    path("Tarif/<int:kp>/delete/", views.Tarif_delete, name="Tarif_delete"),
    path('Operator/new/', views.Operator_new, name='Operator_new'),
    path('Operator/edit/<int:kp>/', views.Operator_edit, name='Operator_edit'),
    path('Operator/delete/<int:kp>/', views.Operator_delete, name='Operator_delete'),
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user')


]

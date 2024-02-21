from django.urls import path

from . import views

app_name = "bidder"
urlpatterns = [
    path("", views.index, name="index"),
    path("help/", views.help, name="help"),
    path("user/", views.user, name="user"),
    path("<int:property_id>/", views.detail, name="detail"),
    path("<int:property_id>/bid/", views.bid, name="bid"),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
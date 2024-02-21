from django.urls import path

from . import views

# pylint: disable=invalid-name
app_name = "bidder"
urlpatterns = [
    path("", views.index, name="index"),
    path("help/", views.help_view, name="help"),
    path("user/", views.user_details, name="user"),
    path("<int:property_id>/", views.detail, name="detail"),
    path("<int:property_id>/bid/", views.bid, name="bid"),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]

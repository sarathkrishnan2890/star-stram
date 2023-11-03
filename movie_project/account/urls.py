from django.urls import path
from . import views
from .views import RegitrationPage



urlpatterns = [
    path('signup/',RegitrationPage.as_view(),name='signnup')
]
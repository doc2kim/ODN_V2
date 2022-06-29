from django.urls import path
from . import views

urlpatterns = [
    path('openapi/', views.OpendataView.as_view(), name="openapi"),
]

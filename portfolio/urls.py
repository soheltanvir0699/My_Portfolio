from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from portfolio import views

urlpatterns = [
    path('', views.index, name='portfolio'),
    path('send/', views.send_email, name='send_email'),
]

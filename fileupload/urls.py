from django.urls import path
from . import views

urlpatterns = [
    # Make the upload view the root URL ('/')
    path('', views.upload_file, name='upload_file'),
]

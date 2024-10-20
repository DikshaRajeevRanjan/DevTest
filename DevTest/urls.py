from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Route the base URL to the file upload view
    path('', include('fileupload.urls')),  # Make the upload page the landing page
]

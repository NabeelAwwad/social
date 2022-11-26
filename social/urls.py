from django.contrib import admin
from django.urls import path, include

app_name = "dwitter"

urlpatterns = [
    path("", include("dwitter.urls")),
    path('admin/', admin.site.urls),
]

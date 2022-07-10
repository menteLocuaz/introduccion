from argparse import Namespace
from django.contrib import admin
from django.urls import path,include
from .views import HomeViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeViews.as_view(),name='home'),
    path('blog/',include('blog.urls'),name='blog'),
]

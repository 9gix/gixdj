from django.shortcuts import render
from django.conf.urls import url
import os

DEBUG = True
SECRET_KEY = 'nothing-is-secret'
ROOT_URLCONF = os.path.splitext(os.path.basename(__file__))[0]
INSTALLED_APPS = (
    # Hahaha, This beats all microframework :D
)
TEMPLATE_DIRS = (
    os.path.dirname(__file__),
)

def index(request):
    return render(request, 'index.html')

urlpatterns = [
    url('^$', index),
]

from django.contrib import admin
import requests


# Register your models here.
response_API = requests.get('https://www.askpython.com/')
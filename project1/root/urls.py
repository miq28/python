from django.urls import path
from .views import index, contact

# controller
urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact')
]
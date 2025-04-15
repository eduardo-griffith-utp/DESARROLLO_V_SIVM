from django.urls import path
from .views import HelloWorldView
urlpatterns = [
 path('hello/', HelloWorldView.as_view(), name='hello-world'),
]

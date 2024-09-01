from django.urls import path
from .views import ShowroomView

urlpatterns = [
    path('', ShowroomView.as_view(), name='showroom'),
]

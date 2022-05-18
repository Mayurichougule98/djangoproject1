from django.urls import path
from . import views
from .views import home, HospitalDetailView

urlpatterns = [
    path('', views.home, name='homepage'),
    path('hospital/<int:pk>', HospitalDetailView.as_view(), name='hospital_detail'),
]
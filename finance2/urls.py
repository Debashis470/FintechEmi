from django.urls import path
from .views import EMI

urlpatterns = [
    path("EMI/", EMI.as_view(), name="Emi"),
]
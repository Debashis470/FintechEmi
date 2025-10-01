"""
URL configuration for Fintrack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from finance1.views import LoanEligibilityView
from finance2.views import EMI  # ensure correct import

def home(request):
    return HttpResponse("<h1>Welcome to Fintrack</h1><p>Go to /api/ to use the API.</p>")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/loan-eligibility/", LoanEligibilityView.as_view(), name="loan-eligibility"),
    path("api/EMI/", EMI.as_view(), name="Emi"),
  # no PK
    path("api/", include("finance.urls")),  # include DRF router URLs
    path("", home, name="home"),
]

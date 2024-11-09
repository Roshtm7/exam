"""
URL configuration for RealEstate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from land import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("realestate/add/",views.RealEstateCreateView.as_view(),name="realestate-add"),
    path("realestate/all/",views.RealEstateListView.as_view(),name="realestate-list"),
    path("realestate/<int:pk>/",views.RealEstateDetailsView.as_view(),name="realestate-details"),
    path("realestate/<int:pk>/remove/",views.RealEstateDeleteView.as_view(),name="realestate-delete"),
    path("realestate/<int:pk>/change/",views.RealEstateUpdateView.as_view(),name="realestate-update")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

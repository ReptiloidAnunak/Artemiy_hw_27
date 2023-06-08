from django.contrib import admin
from django.urls import path

from ads.views import index, CategoriesView, AdsView, AdsDetailView, CategoriesDetaileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('ad/', AdsView.as_view()),
    path('ad/<pk>', AdsDetailView.as_view()),
    path('cat/', CategoriesView.as_view()),
    path('cat/<pk>', CategoriesDetaileView.as_view())
]
from django.urls import path
from . import views

urlpatterns = [
    path('app_searcher/', views.app_searcher, name='searcher'),
    path('keyword_finder/', views.keyword_finder, name='keyword'),
    path('', views.index, name='home')

]
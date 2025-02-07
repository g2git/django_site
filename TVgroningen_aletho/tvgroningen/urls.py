from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('presentations/', views.PresentationListView.as_view(), name='presentations'),
    path('slideshow/', views.slideshow_view, name='slideshow'),
    path('privacy/', views.privacy, name='privacy'),
    path('presentation/<int:pk>', views.PresentationDetailView.as_view(), name='presentation-detail'),
]

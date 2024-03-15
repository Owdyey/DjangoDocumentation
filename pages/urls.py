from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.HomepageView.as_view(),name='homepage'),
    path('about/',views.AboutpageView.as_view(),name='about')
]

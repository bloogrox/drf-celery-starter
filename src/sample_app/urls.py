from django.urls import path
from . import views


urlpatterns = [
    path('samples/', views.SampleListView.as_view(), name='samples'),
]

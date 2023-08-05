from django.urls import path

from . import views
from .email import FeedbackCreateView

app_name = 'headapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('prices', views.prices, name='prices'),
    path('feedback/', FeedbackCreateView.as_view(), name='feedback'),
]
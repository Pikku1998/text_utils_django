from django.urls import path
from text_analyzer.views import homepage

urlpatterns = [
    path('', homepage),
]
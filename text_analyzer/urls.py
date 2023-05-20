from django.urls import path
from text_analyzer.views import homepage,analyzed_text

urlpatterns = [
    path('', homepage),
    path('analyzed-text', analyzed_text),
]
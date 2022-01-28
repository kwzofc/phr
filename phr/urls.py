from django.urls import path
from django.views.generic import TemplateView

app_name = 'phr'

urlpatterns = [
    path('', TemplateView.as_view(template_name="phr/index.html")),
]

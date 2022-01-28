from django.urls import path
from .views import PHRList, PHRDetail

app_name = 'phr_api'

urlpatterns = [
    path('<int:pk>/', PHRDetail.as_view(), name='detail-create'),
    path('', PHRList.as_view(), name='list-create'),
]

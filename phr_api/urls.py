from django.urls import path
from .views import PHRList, PHRDetail, CreateUserView

app_name = 'phr_api'

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='create-user'),
    path('<int:pk>/', PHRDetail.as_view(), name='detail-create'),
    path('', PHRList.as_view(), name='list-create'),
]

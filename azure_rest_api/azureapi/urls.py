from django.urls import path
from .views import EmployeeDetailsViews

urlpatterns = [
    path('emp-details/', EmployeeDetailsViews.as_view()),
    path('emp-details/<int:EMP_ID>', EmployeeDetailsViews.as_view())
]

from django.urls import path
from .views import salary_distribution

urlpatterns = [
    path('chart/', salary_distribution, name='salary_chart'),
]

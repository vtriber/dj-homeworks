from django.urls import path

from measurement.views import SensorView, MeasureView

urlpatterns = [
    path('sensor/<pk>/', SensorView.as_view()),
    path('measure/<pk>/', MeasureView.as_view()),
]
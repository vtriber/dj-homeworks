from django.urls import path

from measurement.views import SensorsView, MeasurementsView, SensorDetailView

urlpatterns = [
    path('sensors/<pk>', SensorsView.as_view()),
    path('sensors/', SensorsView.as_view()),
    path('measurements/', MeasurementsView.as_view()),
    path('sensors/<pk>/', SensorDetailView.as_view()),
]
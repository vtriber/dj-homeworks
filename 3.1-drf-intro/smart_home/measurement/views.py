from rest_framework.decorators import api_view
from rest_framework.mixins import CreateModelMixin
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView, \
    RetrieveAPIView

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer, \
    AddMeasurementSerializer
from rest_framework.response import Response


class SensorsView(ListAPIView, CreateAPIView, RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, Sensor.name, Sensor.description)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class MeasurementsView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = AddMeasurementSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SensorDetailView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
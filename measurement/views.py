from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer


class SensorView(RetrieveUpdateAPIView):
    serializer_class = SensorDetailSerializer
    queryset = Sensor.objects.all()


class SensorsView(ListCreateAPIView):
    serializer_class = SensorDetailSerializer
    queryset = Sensor.objects.all()


class MeasurementsView(CreateAPIView):
    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()

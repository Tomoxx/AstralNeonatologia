from rest_framework.viewsets import ModelViewSet
from core.api.serializers import RecienNacidoSerializer
from core.models import RecienNacido


class RecienNacidoApiViewSet(ModelViewSet):
    serializer_class = RecienNacidoSerializer
    queryset = RecienNacido.objects.all()
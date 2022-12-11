from rest_framework.serializers import ModelSerializer
from core.models import RecienNacido


class RecienNacidoSerializer(ModelSerializer):
    class Meta:
        model = RecienNacido
        fields = ['id', 'nombre', 'paterno', 'materno','fecha_nacimiento', 'direccion', 'deAlta', 'altas', 'alta', 'padres']
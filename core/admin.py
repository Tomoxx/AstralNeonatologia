from django.contrib import admin

from core.models import Sector
from core.models import Cama
from core.models import Evolucion
from core.models import RecienNacido

# Register your models here.

admin.site.register(Sector)
admin.site.register(Cama)
admin.site.register(Evolucion)
admin.site.register(RecienNacido)

#superadmin= coordinadora pass= 1234
#TODAS LAS CONTRASEÑAS SON 1234
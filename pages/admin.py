from django.contrib import admin

from .models import Promotora
admin.site.register(Promotora)

from .models import Cliente
admin.site.register(Cliente)

from .models import Tasting
admin.site.register(Tasting)

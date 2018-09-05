from django.contrib import admin
from .models import Key,keyHistory,TempKeys

admin.site.register(Key)
admin.site.register(keyHistory)
admin.site.register(TempKeys)
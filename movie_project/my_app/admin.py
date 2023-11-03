from django.contrib import admin

from .models import Films, Series, English, Kids


# Register your models here.
admin.site.register(Films)
admin.site.register(Series)
admin.site.register(English)
admin.site.register(Kids)

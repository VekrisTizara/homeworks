from django.contrib import admin

from .models import Painting, PaintingStyle, PaintingMaterial

admin.site.register(Painting)
admin.site.register(PaintingStyle)
admin.site.register(PaintingMaterial)
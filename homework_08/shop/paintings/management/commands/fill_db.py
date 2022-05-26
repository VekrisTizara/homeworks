from django.core.management.base import BaseCommand

from paintings.models import PaintingMaterials


class Command(BaseCommand):

    def handle(self, *args, **options):
        materials = ['ink', 'watercolor', 'oil', 'acrylic']
        for material in materials:
            PaintingMaterials.objects.get_or_create(name=material)
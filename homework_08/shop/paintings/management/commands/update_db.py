from django.core.management.base import BaseCommand

from paintings.models import Painting, PaintingDetail


class Command(BaseCommand):

    def handle(self, *args, **options):
        update_paintings = Painting.objects.filter(animaldetail__isnull=True)

        for painting in update_paintings:
            PaintingDetail.objects.create(
                painting=painting,
                details='will be soon filled'
            )
            print(f'for {animal} detail created')
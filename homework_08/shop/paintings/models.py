from django.db import models


class PaintingStyle(models.Model):
    name = models.CharField(max_length=32, unique=True)
    desc = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}'


class Painting(models.Model):
    name = models.CharField(max_length=64)
    style = models.ForeignKey(PaintingStyle, on_delete=models.CASCADE, null=True)
    canvas_type = models.CharField(max_length=32)
    diagonal = models.FloatField(null=True)
    height = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'Painting: {self.name}'

    def get_materials(self):
        material = self.paintingmaterial_set.all()
        return ', '.join(map(str, material))


class PaintingMaterial(models.Model):
    name = models.CharField(max_length=64, unique=True)
    painting = models.ManyToManyField(Painting)

    def __str__(self):
        return self.name



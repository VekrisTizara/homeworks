# Generated by Django 3.2 on 2022-05-24 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paintings', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PaintingMaterials',
            new_name='PaintingMaterial',
        ),
    ]
# Generated by Django 4.1.3 on 2022-12-11 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_estado_reciennacido_dealta_reciennacido_alta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evolucion',
            name='peso',
            field=models.FloatField(),
        ),
    ]
# Generated by Django 3.2.8 on 2021-11-03 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uk_regions', '0004_centerregional'),
    ]

    operations = [
        migrations.AddField(
            model_name='centerregional',
            name='level',
            field=models.PositiveIntegerField(default=2, verbose_name='Уровень'),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2 on 2023-09-23 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_brand_universe'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='has_themes',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]

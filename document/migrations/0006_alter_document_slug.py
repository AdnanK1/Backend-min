# Generated by Django 4.1 on 2022-08-16 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0005_document_slug_alter_document_station'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='slug',
            field=models.SlugField(max_length=255, unique_for_date='date'),
        ),
    ]

# Generated by Django 4.1 on 2022-08-17 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0006_alter_document_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
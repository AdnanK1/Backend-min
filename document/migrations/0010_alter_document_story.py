# Generated by Django 4.1 on 2022-08-17 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0009_document_story'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='story',
            field=models.TextField(blank=True, null=True),
        ),
    ]
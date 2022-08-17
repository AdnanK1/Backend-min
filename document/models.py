from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

# Create your models here.
class Document(models.Model):
    catch_word = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    options = (
        ('Mombasa', 'Mombasa'),
        ('Kwale', 'Kwale'),
        ('Kilifi', 'Kilifi'),
        ('Tana River', 'Tana River'),
        ('Lamu', 'Lamu'),
        ('Taita-Taveta', 'Taita-Taveta'),
        ('Garissa', 'Garissa'),
        ('Wajir', 'Wajir'),
        ('Mandera', 'Mandera'),
        ('Marsabit', 'Marsabit'),
        ('Isiolo', 'Isiolo'),
        ('Meru', 'Meru'),
        ('Tharaka-Nithi', 'Tharaka-Nithi'),
        ('Embu', 'Embu'),
        ('Kitui', 'Kitui'),
        ('Machakos', 'Machakos'),
        ('Makueni', 'Makueni'),
        ('Nyandarua', 'Nyandarua'),
        ('Nyeri', 'Nyeri'),
        ('Kirinyaga', 'Kirinyaga'),
        ('Murang\'a', 'Murang\'a'),
        ('Kiambu', 'Kiambu'),
        ('Turkana', 'Turkana'),
        ('West Pokot', 'West Pokot'),
        ('Samburu', 'Samburu'),
        ('Trans-Nzoia', 'Trans-Nzoia'),
        ('Uasin Gishu', 'Uasin Gishu'),
        ('Elgeyo-Marakwet', 'Elgeyo-Marakwet'),
        ('Nandi', 'Nandi'),
        ('Baringo', 'Baringo'),
        ('Laikipia', 'Laikipia'),
        ('Nakuru', 'Nakuru'),
        ('Narok', 'Narok'),
        ('Kajiado', 'Kajiado'),
        ('Kericho', 'Kericho'),
        ('Bomet', 'Bomet'),
        ('Kakamega', 'Kakamega'),
        ('Vihiga', 'Vihiga'),
        ('Bungoma', 'Bungoma'),
        ('Busia', 'Busia'),
        ('Siaya', 'Siaya'),
        ('Kisumu', 'Kisumu'),
        ('Homa Bay', 'Homa Bay'),
        ('Migori', 'Migori'),
        ('Kisii', 'Kisii'),
        ('Nyamira', 'Nyamira'),
        ('Nairobi', 'Nairobi'),
    )
    station = models.CharField(
        max_length=80, choices=options, default='', null=True)
    date = models.DateField()
    author = models.CharField(max_length=255)
    heading = models.CharField(max_length=255)
    story = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.catch_word)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.catch_word)

    class Meta:
        ordering = ['-created', '-updated']


def slugify_instance(instance, save=False):
    slug = slugify(instance.catch_word)
    qs = Document.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        slug = f"{slug}-{qs.count() + 1}"
    instance.slug = slug
    if save:
        instance.save()
    return instance


def document_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance(instance, save=True)


pre_save.connect(document_pre_save, sender=Document)


def document_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')
    if created:
        slugify_instance(instance, save=True)


post_save.connect(document_post_save, sender=Document)

class Images(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='document')
    images = models.ImageField(
        upload_to='image/%Y/%m/%d/', default="image", blank=True, null=True)
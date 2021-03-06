from django.db import models

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True) # noqa

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

from __future__ import unicode_literals
from django.db import models

class Supercategory(models.Model):
    name = models.TextField()
    label = models.TextField()

    def __str__(self):
        return ' '.join([self.name, self.label])

    def __unicode__(self):
        return self.__str__()

    class Meta:
        ordering = ['name']

class Category(models.Model):
    name = models.TextField()
    label = models.TextField()
    supercat = models.ForeignKey(Supercategory, related_name='cat_supercat')

    def __str__(self):
        return ' '.join([self.name, self.label, self.supercat.name])

    def __unicode__(self):
        return self.__str__()

    class Meta:
        ordering = ['name']

class Thing(models.Model):
    name = models.CharField(max_length=255,)
    label = models.CharField(max_length=255,)
    cat = models.ForeignKey(Category, related_name='host_cat')

    def __str__(self):
        return ' '.join([self.name, self.label, self.cat.name])

    def __unicode__(self):
        return self.__str__()

    class Meta:
        ordering = ['name']

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Info(models.Model):
    region = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    destino = models.CharField(max_length=50)
    nombree = models.CharField(db_column='nombreE', primary_key=True, max_length=50)  # Field name made lowercase.
    calle = models.CharField(max_length=50)
    num = models.CharField(max_length=10)
    otro = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    web = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'info'

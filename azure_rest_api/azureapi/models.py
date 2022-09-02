# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import date
from django import utils


class EmpDetails(models.Model):
    EMP_ID = models.CharField(max_length=50, blank=False, null=False, primary_key=True)
    EMP_NAME = models.CharField(max_length=50, blank=False, null=False)
    DEPT = models.CharField(max_length=50, blank=False, null=False)
    DESIGNATION = models.CharField(max_length=50, blank=False, null=False)
    RM = models.CharField(max_length=50, blank=True, null=True)
    BU = models.CharField(max_length=50, blank=True, null=True)
    DOJ = models.DateTimeField(blank=False, null=False, default=utils.timezone.now)
    CTC = models.DecimalField(max_digits=18, decimal_places=0, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'emp_details'

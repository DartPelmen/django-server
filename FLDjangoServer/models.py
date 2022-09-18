from django.db import models


# Create your models here.
class Table1(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID')  # Field name made lowercase.
    data1 = models.CharField(db_column='Data1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data2 = models.CharField(db_column='Data2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data3 = models.CharField(db_column='Data3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    data4 = models.CharField(db_column='Data4', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'table1'


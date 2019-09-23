from django.db import models


class Bin1(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateTimeField()
    value=models.IntegerField(blank=False)


class Bin2(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateTimeField()
    value=models.IntegerField(blank=False)

class Bin3(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateTimeField()
    value=models.IntegerField(blank=False)

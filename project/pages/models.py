from django.db import models
from django.contrib.postgres.fields import ArrayField


class MaklerHouse(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    address = models.CharField(max_length=255, unique=True)
    img = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    description = models.TextField( default="")
    low_img = models.TextField( default="")
    high_img = models.TextField( default="")
    type = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    floor_area = models.CharField(max_length=255)
    plot_area = models.CharField(max_length=255)
    municipality = models.CharField(max_length=255)
    costs = models.TextField(default="")
    vr_img = models.TextField( default="")
    date_added = models.DateTimeField()

    class Meta:
        db_table = 'maklar_houses'

class FkHouse(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    address = models.CharField(max_length=255, unique=True)
    img = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    description = models.TextField( default="")
    low_img = models.TextField( default="")
    high_img = models.TextField( default="")
    type = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    floor_area = models.CharField(max_length=255)
    plot_area = models.CharField(max_length=255)
    municipality = models.CharField(max_length=255)
    costs = models.TextField(default="")
    vr_img = models.TextField( default="")
    date_added = models.DateTimeField()

    class Meta:
        db_table = 'fk_houses'

class LyyskiHouse(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    address = models.CharField(max_length=255, unique=True)
    img = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    description = models.TextField( default="")
    low_img = models.TextField( default="")
    high_img = models.TextField( default="")
    type = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    floor_area = models.CharField(max_length=255)
    plot_area = models.CharField(max_length=255)
    municipality = models.CharField(max_length=255)
    costs = models.TextField(default="")
    vr_img = models.TextField( default="")
    date_added = models.DateTimeField()

    class Meta:
        db_table = 'lyyski_houses'

class FormHouse(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    address = models.CharField(max_length=255, unique=True)
    img = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    description = models.TextField( default="")
    low_img = models.TextField( default="")
    high_img = models.TextField( default="")
    type = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    floor_area = models.CharField(max_length=255)
    plot_area = models.CharField(max_length=255)
    municipality = models.CharField(max_length=255)
    costs = models.TextField(default="")
    vr_img = models.TextField( default="")
    date_added = models.DateTimeField()

    class Meta:
        db_table = 'form_houses'


class AveragePrice(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    table_name = models.TextField()
    individual_average_prices = ArrayField(models.FloatField())
    overall_average_price = models.FloatField()

    def __str__(self):
        return f"{self.date} - {self.table_name}"

    class Meta:
        db_table = 'average_prices'  # Set the table name for the AveragePrice model
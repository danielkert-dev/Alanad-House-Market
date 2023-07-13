from django.db import models

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
    #costs = models.TextField(default="")
    vr_img = models.TextField( default="")
    date_added = models.DateTimeField()

    class Meta:
        db_table = 'maklar_houses'

from pydoc import describe
from django.db import models

class Top(models.Model):
    category = models.CharField(max_length=5, default='T')
    itemname = models.CharField(max_length=255, default='NEWTOP')
    price = models.IntegerField(null=True)
    photo = models.ImageField(upload_to="images/", null=True, blank=True)
    describe = models.CharField(max_length=255, default='des')

    def __str__(self):
        return self.itemname

class Bottom(models.Model):
    category = models.CharField(max_length=5, default='B')
    itemname = models.CharField(max_length=255, default='NEWBOTTOM')
    price = models.IntegerField(null=True)
    photo = models.ImageField(upload_to="media/", null=True, blank=True)
    describe = models.CharField(max_length=255, default='des')

    def __str__(self):
        return self.itemname

class Acc(models.Model):
    category = models.CharField(max_length=5, default='A')
    itemname = models.CharField(max_length=255, default='NEWACC')
    price = models.IntegerField(null=True)
    photo = models.ImageField(upload_to="media/", null=True, blank=True)
    describe = models.CharField(max_length=255, default='des')

    def __str__(self):
        return self.itemname

class Dress(models.Model):
    category = models.CharField(max_length=5, default='D')
    itemname = models.CharField(max_length=255, default='NEWDRESS')
    price = models.IntegerField(null=True)
    photo = models.ImageField(upload_to="media/", null=True, blank=True)
    describe = models.CharField(max_length=255, default='des')

    def __str__(self):
        return self.itemname
Top.image = 'images/cattop.jpg'
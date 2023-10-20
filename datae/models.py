from django.db import models

class crudst(models.Model):
    stname = models.CharField(max_length=100)
    stemail = models.CharField(max_length=100)
    staddress = models.CharField(max_length=100)
    stmobile = models.BigIntegerField()
    stgender = models.CharField(max_length=1)
    ststart = models.CharField(max_length=100)
    stend = models.CharField(max_length=100)
    stbank = models.BigIntegerField()
    staadhar = models.BigIntegerField()
    strfid = models.CharField(max_length=100)

class RFIDInfo(models.Model):
    rfid = models.CharField(max_length=100)
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    route = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

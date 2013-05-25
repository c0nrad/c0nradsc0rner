from django.db import models

# Create your models here.
class DepositAddress(models.Model):
    address = models.CharField(blank=True, max_length=50)
    fromaddress = models.CharField(blank=True, max_length=50)
    balance = models.DecimalField(max_digits=7, decimal_places=5)
    
    def __unicode__(self):
        return "%s from:%s %s" % (str(address), str(fromaddress), str(balance))

class Round(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    address = models.ForeignKey('bitcoin.DepositAddress')
    betAmount = models.DecimalField(max_digits=7, decimal_places=5)
    isWin = models.BooleanField()

    def __unicode__(self):
        return "%s: %s %s %s" % (str(datetime), str(betAmount), str(isWin)) 

    

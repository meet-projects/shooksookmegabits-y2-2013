from django.db import models

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length = 50)
    storeType = models.CharField(max_length = 20)
    adress = models.CharField(max_length = 50)
    info = name = models.CharField(max_length = 1000)

    def storeInfo(self):
        return HttpResopnse("Name: " + self.name + '/n' + "Store Type: " + self.storeType + '/n' + "Adress: "+ slef.adress + '/n' + "Info : " +self.info)


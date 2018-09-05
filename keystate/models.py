from django.db import models


# Create your models here.
class Key(models.Model):
    keytag = models.CharField(max_length=100)
    keyname = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    curr_user = models.CharField(max_length=60,default='aymen')
    key_categ = models.CharField(max_length=50,default='white')
    keystate_in = models.BooleanField(default=True)

    def __str__(self):
        return 'keytag number is ' + self.keytag + ' - ' + self.key_categ

class keyHistory(models.Model):
    keytag = models.ForeignKey(Key,on_delete=models.CASCADE)
    date_checkout = models.DateField()
    user_checkout = models.CharField(max_length=100)
    state_checkout = models.BooleanField(default=True)

    def __str__(self):
        return str(self.keytag_id)


class TempKeys(models.Model):
    keytag = models.CharField(max_length=100)

    def __str__(self):
        return 'keytag number is ' + self.keytag
from django.db import models

# Create your models here.
class AccountTypes(models.Model):
    name = models.CharField(max_length=200)
    normbalance = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = "Account Types"

    def __str__(self):
        return self.name


class Accounts(models.Model):
    class Meta:
        verbose_name_plural = "Accounts"
    account = models.IntegerField(unique=True)
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(AccountTypes, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
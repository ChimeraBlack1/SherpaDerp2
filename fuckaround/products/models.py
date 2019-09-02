from django.db import models
from accounting.models import Accounts

# Create your models here.
class Products(models.Model):
    class Meta:
        verbose_name_plural = "Products"
    
    account = models.ForeignKey(Accounts, on_delete=models.DO_NOTHING)
    number = models.IntegerField(unique=True, default=1, null=True)
    name = models.CharField(max_length=200)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name
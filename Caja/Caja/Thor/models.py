from django.db import models


class Sale(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    amount = models.IntegerField()   
    payment=models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

    def total(self):
        return self.price*self.amount
    def change(self):
        return max(self.payment - self.total(), 0)
    


from django.db import models
from catalog.models import Book
from catalog.validators import validar_gt_0
from django.utils import timezone

# Create your models here.

class Order(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    email = models.EmailField(max_length=100)

    address = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=50)
    city = models.CharField(max_length=100)

    created = models.DateTimeField(default=timezone.now())
    updated = models.DateTimeField(default=timezone.now())

    paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        super(Order, self).save(*args, **kwargs)

    def get_total_cost(self):

        total_price = 0
        
        for i in self.items.all():
            total_price += i.book.price * i.quantity
        
        return total_price

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)


class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)

    price = models.DecimalField(
            default=0,
            decimal_places=2,
            max_digits=10,
            editable=False
        )

    quantity = models.IntegerField(default=1, validators=[validar_gt_0])

    def save(self, *args, **kwargs):
        self.price = self.book.price
        super(OrderItem, self).save(*args, **kwargs)

    def __str__(self):
        return '%s -  %s, %d' % (self.order, self.book, self.quantity)
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ValidationError
from .models import OrderItem

@receiver(post_save, sender=OrderItem) # signal to reduce stock when an order is placed
def reduce_stock(sender, instance, created, **kwargs):
    if created:  # check if the order item was created
        product = instance.product
        if product.stock_Quantity >= instance.quantity:
            product.stock_Quantity -= instance.quantity
            product.save() # save the updated product
        else:
            raise ValidationError(
                f"Not enough stock for product '{product.name}'. Available stock: {product.stock_Quantity}, requested: {instance.quantity}."
            ) # raise validation error if there is not enough stock
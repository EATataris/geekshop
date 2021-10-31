from django.db import models


from users.models import User
from products.models import Product
# Create your models here.


# class BasketQuerySet(models.QuerySet):
#
#     def delete(self):
#         for item in self:
#             item.product.quantity += item.quantity
#             item.product.save()
#         super().delete()


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    # objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    def total_sum(self):
        baskets = Basket.objects.filter(user=self.user)
        return  sum(basket.sum() for basket in baskets)

    def total_quantity(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.quantity for basket in baskets)

    # def delete(self, using=None, keep_parents=False):
    #     self.product.quantity += self.quantity
    #     self.product.save()
    #     super().delete()
    #
    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     if self.pk:
    #         self.product.quantity -= self.quantity - self.get_item(int(self.pk))
    #     else:
    #         self.product.quantity -= self.quantity
    #     self.product.save()
    #     super().save()

    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk).quantity

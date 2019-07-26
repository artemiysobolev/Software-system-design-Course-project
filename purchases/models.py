from django.db import models
from django.db.models.signals import post_save
from excursions.models import Excursion


class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name = 'Статус покупки'
        verbose_name_plural = 'Статусы покупок'


class Purchase(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #total price for all products in order
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Покупка %s %s" % (self.id, self.status.name)

    def save(self, *argc, **kwargs):
        super(Purchase, self).save(*argc, **kwargs)

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'


class ExcursionInPurchase(models.Model):
    purchase = models.ForeignKey(Purchase, blank=True, null=True, default=None, on_delete=models.CASCADE)
    excursion = models.ForeignKey(Excursion, blank=True, null=True, default=None, on_delete=models.CASCADE)
    # nmbr = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return "%s" % self.excursion.name


    def save(self, *argc, **kwargs):
        price = self.excursion.price
        self.price = price
        # self.total_price = self.nmbr * self.price_per_item

        super(ExcursionInPurchase, self).save(*argc,**kwargs)

    class Meta:
        verbose_name = 'Экскурсия в заказе'
        verbose_name_plural = 'Экскурсии в заказе'

def excursion_in_purchase_post_save(sender, instance, created, **kwargs):
    purchase = instance.purchase
    all_excursions_in_purchase = ExcursionInPurchase.objects.filter(purchase=purchase, is_active=True)

    purchase_total_price = 0
    for item in all_excursions_in_purchase:
        purchase_total_price += item.price

    instance.purchase.total_price = purchase_total_price
    instance.purchase.save(force_update=True)

post_save.connect(excursion_in_purchase_post_save, sender=ExcursionInPurchase)

class ExcursionInBasket(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    purchase = models.ForeignKey(Purchase, blank=True, null=True, default=None, on_delete=models.CASCADE)
    excursion = models.ForeignKey(Excursion, blank=True, null=True, default=None, on_delete=models.CASCADE)
    # nmbr = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return "%s" % self.excursion.name

    def save(self, *argc, **kwargs):
        price = self.excursion.price
        self.price = price
        # self.total_price = self.nmbr * self.price_per_item

        super(ExcursionInBasket, self).save(*argc,**kwargs)

    class Meta:
        verbose_name = 'Экскурсия в корзине'
        verbose_name_plural = 'Экскурсии в корзине'

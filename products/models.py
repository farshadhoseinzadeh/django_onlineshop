from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField


class Product(models.Model):
    title = models.CharField(verbose_name=_('Product Title'), max_length=100)
    short_description = models.TextField(verbose_name=_('Product Short Description'), blank=True)
    description = RichTextField(verbose_name=_('Product Description'))
    price = models.PositiveIntegerField(verbose_name=_('Product Price'), default=0)
    active = models.BooleanField(verbose_name=_('Active or Hidden'), default=True)
    image = models.ImageField(verbose_name=_('Product Image'), upload_to='product/product_cover/', blank=True)

    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])


class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    PRODUCT_STARS = [
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect')),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments',
                                verbose_name=_('Product Name'))
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments',
                               verbose_name=_('Comment Author'))
    body = models.TextField(verbose_name=_('Your Comment'))
    stars = models.CharField(max_length=10, choices=PRODUCT_STARS, verbose_name=_('Comment Score'))

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    active = models.BooleanField(verbose_name=_('Active or Hidden'), default=True)

    # Manager
    objects = models.Manager
    active_comments_manager = ActiveCommentManager()

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])

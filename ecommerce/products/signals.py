from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Product
from .utils import unique_string_generator


@receiver(pre_save, sender=Product)
def create_slug(sender, instance, **kwargs):
    print("Slug created")
    if not instance.slug:
        print(unique_string_generator(instance))
        instance.slug = unique_string_generator(instance)


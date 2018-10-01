from django.apps import AppConfig


class ProductsConfig(AppConfig):
    name = 'products'

    def ready(self):
        print("\n\n Products ready", flush=True)
        import products.signals
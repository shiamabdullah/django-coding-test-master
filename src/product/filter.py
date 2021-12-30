from product.models import Product, Variant
import django_filters

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields =  {'title':['icontains'],
                   'id':['icontains']}
                   
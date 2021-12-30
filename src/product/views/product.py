from django.views import generic

from product.models import Product, Variant
from product.models import ProductVariant, ProductVariantPrice
from django.views.generic import ListView
from product.filter import ProductFilter
class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context
    

class ProductListView(ListView):
    template_name = "products/list.html"
    model=Product
    paginate_by= 5
    context_object_name = 'products'
    
    def get_queryset(self):
        filter_string = {}
        print(self.request.GET)
        for key in self.request.GET:
            if self.request.GET.get(key):
                filter_string[key] = self.request.GET.get(key)
        return Product.objects.filter(**filter_string)
    
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        
        variant_types = Variant.objects.values()
        product_variant = ProductVariant.objects.values().order_by('variant_id')
        product_variant_price = ProductVariantPrice.objects.values()
        context['product_filter']= ProductFilter(self.request.GET,queryset=self.get_queryset())
        
        context['product_variant'] = list(product_variant.all())
        context['variant_types'] = list(variant_types.all())
        context['product_variant_price'] = list(product_variant_price.all())
        context['request'] = ''
        
        if self.request.GET:
            context['request'] = self.request.GET['title__icontains']
        return context


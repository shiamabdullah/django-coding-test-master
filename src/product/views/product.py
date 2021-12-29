from django.views import generic

from product.models import Product, Variant
from product.models import ProductVariant, ProductVariantPrice

class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context
    
from django.views.generic import TemplateView

class ProductListView(TemplateView):
    template_name = "products/list.html"
# 'id', 'product', 'product_id', 'product_variant_one', 'product_variant_three', 'product_variant_two',
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        product = Product.objects.filter().values('id', 'title','description')
        
        variant_types = Variant.objects.filter().values()
        product_variant = ProductVariant.objects.filter().values().order_by('variant_id')
        product_variant_price = ProductVariantPrice.objects.filter().values()
        
        context['products'] = list(product.all())
        context['product_variant'] = list(product_variant.all())
        context['variant_types'] = list(variant_types.all())
        context['product_variant_price'] = list(product_variant_price.all())
        
        return context
    


# class ProductView(BaseVariantView, generics.ListView):
#     template_name = 'variants/list.html'
#     paginate_by = 10

#     def get_queryset(self):
#         filter_string = {}
#         print(self.request.GET)
#         for key in self.request.GET:
#             if self.request.GET.get(key):
#                 filter_string[key] = self.request.GET.get(key)
#         return Variant.objects.filter(**filter_string)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['product'] = True
#         context['request'] = ''
#         if self.request.GET:
#             context['request'] = self.request.GET['title__icontains']
#         return context

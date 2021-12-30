from django.views import generic
from django.views.generic.edit import CreateView

from product.models import Product, Variant
from product.models import ProductVariant, ProductVariantPrice
from django.views.generic import ListView
from product.filter import ProductFilter
from django.db.models import Q

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
    model= Product
    paginate_by= 5
    context_object_name = 'products'
    
    def get_queryset(self):
        filter_val=self.request.GET.get("title_filter","")
        date_filter_val=self.request.GET.get("date_filter","")
        print(filter_val,date_filter_val)

        if filter_val!="":
            pro=Product.objects.filter(Q(title__icontains=filter_val) & Q(created_at__contains=date_filter_val))
            
        else:
            pro=Product.objects.all()
        return pro
   
 
    
    def get_context_data(self, **kwargs):
        
        context = super(ProductListView, self).get_context_data(**kwargs)
        
        context['title_filter']= self.request.GET.get('title_filter','')
        context['date_filter']= self.request.GET.get('date_filter','')

        
        variants = Variant.objects.all()
        
        product_variant = ProductVariant.objects.all()
        product_variant_distinct = ProductVariant.objects.values('variant_title','variant').distinct()
        
        product_variant_price = ProductVariantPrice.objects.all()

        context['product_variant'] = product_variant
        context['product_variant_distinct'] = product_variant_distinct
        context['variants'] = variants
        context['product_variant_price'] = product_variant_price
   
        
        return context

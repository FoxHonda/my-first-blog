from django.shortcuts import render
from .models import Product
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from usext.models import UserExtends

class ProductListView(LoginRequiredMixin, generic.ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['vip'] = UserExtends.objects.get(user=self.request.user).vip 
        return context

class ProductDetailView(generic.DetailView):
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        user_id = 'U_user_id'
        product_id = 'P_product_id'
        current_unix_date = 'D_current_unix_date'
        context['pay_id_no'] = user_id+product_id+current_unix_date 
        return context
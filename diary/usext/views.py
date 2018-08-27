from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .models import UserExtends
from django.urls import reverse_lazy
from diary.settings import DEFAULT_IMG_FOR_POST_BACKGROUND
from .forms import UserExtendsForm

class UserExtendsUpdate(LoginRequiredMixin,UpdateView):
	model = UserExtends
	form_class = UserExtendsForm
	success_url = reverse_lazy('profile')

	def get_object(self):
		obj = UserExtends.objects.get(user = self.request.user)
		return obj

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		kwargs['def_img'] = DEFAULT_IMG_FOR_POST_BACKGROUND
		return kwargs

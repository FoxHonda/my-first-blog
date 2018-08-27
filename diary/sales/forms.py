from django import forms
from django.core.exceptions import ValidationError

def isInt(value):
	try:
		int(value)
		return True
	except ValueError:
		return False


class CheckOutForm(forms.Form):
    
	product = forms.IntegerField()

	def clean_product(self):
		data = self.cleaned_data['product']
		if not isInt(data):
			raise ValidationError('Wrong product ID')
		return data
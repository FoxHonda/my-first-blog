from django.forms import ModelForm
from .models import UserExtends

class UserExtendsForm(ModelForm):

    class Meta:
        model = UserExtends
        fields = ['avatar']

    def __init__(self, def_img, *args, **kwargs):
        self.def_img = def_img
        super().__init__(*args, **kwargs)
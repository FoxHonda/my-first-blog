from django.forms import ModelForm, inlineformset_factory
from .models import Post, PostImages
import re
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User
from diary.settings import USEXT_TEXT_LENGTH_COMMON, USEXT_FILES_COUNT_VIP, USEXT_FILES_COUNT_COMMON,USEXT_TEXT_LENGTH_VIP
from django.db.models import Count

litnum_re = re.compile(r"^\w+$")

class PostImagesForm(ModelForm):
    
    class Meta:
        model = PostImages
        fields = ['image','order']



class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['text','tags']

    def __init__(self, vip, maxsymb, *args, **kwargs):
        self.vip = vip
        self.maxsymb = maxsymb
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(PostForm, self).clean()
        cleaned_tags = cleaned_data.get("tags")
        cleaned_text = cleaned_data.get("text")
        # cleaned_files = cleaned_data.get("files")
        # print('/'*80)
        # print(cleaned_files)
        if self.vip < timezone.now() and len(cleaned_text) > USEXT_TEXT_LENGTH_COMMON:
            raise forms.ValidationError("Пост длинее 400 символов доступен только ВИП пользователям.")
        elif self.vip >= timezone.now() and len(cleaned_text) > USEXT_TEXT_LENGTH_VIP:
            raise forms.ValidationError("Пост должен быть менее 4000 символов.")

        tag_count = 0
        for tag in cleaned_tags:
            tag_count +=1
            if tag_count > 5:
                raise forms.ValidationError("Не может быть больше 5 тегов")
            if len(tag) < 3 or len(tag) > 50 or not litnum_re.search(tag):
                raise forms.ValidationError("Tag's length must be beetwen 3 and 50 symbols and contain letters, numbers and underscores.")      		


PostImagesFormSet = inlineformset_factory(Post, PostImages, form=PostImagesForm, fields=('__all__'), extra=1, max_num=USEXT_FILES_COUNT_COMMON)
PostImagesFormSetVip = inlineformset_factory(Post, PostImages, form=PostImagesForm, fields=('__all__'), extra=1, max_num=USEXT_FILES_COUNT_VIP)

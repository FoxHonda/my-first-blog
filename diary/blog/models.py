from django.db import models
from django.urls import reverse
# from authentication.models import Account
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase
import uuid 
from diary.settings import DEFAULT_IMG_FOR_POST_BACKGROUND
from usext.models import UserExtends

class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    # If you only inherit GenericUUIDTaggedItemBase, you need to define
    # a tag field. e.g.
    # tag = models.ForeignKey(GenericUUIDTaggedItemBase, related_name="uuid_tagged_items", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Уникальный ИД для поста')
    text = models.TextField(max_length=4000, help_text='Введите текст', null=False, blank=False)
    post_date = models.DateTimeField(auto_now_add=True, help_text='Дата публикации')
    modify_date = models.DateTimeField(auto_now=True, help_text='Дата редактирования')
    user = models.ForeignKey(User, default=1,on_delete=models.CASCADE, blank=False)
    tags = TaggableManager(through=UUIDTaggedItem,blank=True)
    CURRENT_STATUS = (
        ('d', 'Deleted'),
        ('a', 'Active'),
        ('h', 'Hidden'),
        ('b', 'Banned'),
    )

    status = models.CharField(max_length=1, choices=CURRENT_STATUS, blank=True, default='a', help_text='Статус поста')

    class Meta:
    	ordering = ['-post_date']

    def __str__(self):

    	return "%s (%s)" % (self.id,self.post_date)

    def get_absolute_url(self):

        return reverse('post-detail', args=[str(self.id)])

    @property
    def get_post_bg(self):
        user_data = UserExtends.objects.get(user = self.user)
        if user_data.avatar is None or user_data.avatar == '':
            image_url = DEFAULT_IMG_FOR_POST_BACKGROUND
        else:
            image_url = user_data.avatar.url
        return image_url



class PostImages(models.Model):
    image = models.ImageField(blank=False)
    post = models.ForeignKey('Post',on_delete=models.CASCADE)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order',]
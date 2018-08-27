from django.shortcuts import render, redirect
from .models import Post, PostImages, UUIDTaggedItem
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostForm, PostImagesFormSet, PostImagesFormSetVip
from django.contrib.auth.decorators import login_required
from usext.models import UserExtends
from django.utils import timezone
from django.db.models import Count
from taggit.models import Tag
from diary.settings import TAG_LIMIT, USEXT_TEXT_LENGTH_COMMON,USEXT_TEXT_LENGTH_VIP

def index(request):
    
    num_posts=Post.objects.all().count()
    num_images=PostImages.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_posts':num_posts,'num_images':num_images},
    )

def perm_denied(request):
    return render(request,'blog/perm_denied.html')

def tag_cloud(user):
    tag_cloud = Tag.objects.filter(id__in=UUIDTaggedItem.objects.values('tag').filter(object_id__in=Post.objects.filter(user=user)).annotate(dcount=Count('tag')).values('tag').order_by('-dcount')[:20])
    return tag_cloud

@login_required
def search_by_tag(request, tag):
    posts_with_tag = Post.objects.filter(user=request.user).filter(tags__name__in=[tag]).order_by('-post_date')
    t_cloud = tag_cloud(request.user) #Tag.objects.filter(id__in=UUIDTaggedItem.objects.values('tag').filter(object_id__in=Post.objects.filter(user=request.user)).annotate(dcount=Count('tag')).values('tag').order_by('-dcount')[:TAG_LIMIT])
    return render(request, 'blog/tags.html', {'posts_with_tag': posts_with_tag, 'search_tag':tag, 'tag_cloud':t_cloud})


@login_required
def search(request):
    if 'q' in request.GET and request.GET['q']:
        tag = request.GET['q']
        posts_with_tag = Post.objects.filter(user=request.user).filter(tags__name__in=[tag]).order_by('-post_date')
        t_cloud = tag_cloud(request.user)
        return render(request, 'blog/tags.html', {'posts_with_tag': posts_with_tag, 'search_tag':tag, 'tag_cloud':t_cloud})
    else:
        t_cloud = tag_cloud(request.user)
        return render(request, 'blog/tags.html', {'posts_with_tag': [], 'search_tag':'', 'tag_cloud':t_cloud})


class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user).order_by('-post_date')

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['tag_cloud'] = tag_cloud(self.request.user) #Tag.objects.filter(id__in=UUIDTaggedItem.objects.values('tag').filter(object_id__in=Post.objects.filter(user=self.request.user)).annotate(dcount=Count('tag')).values('tag').order_by('-dcount')[:TAG_LIMIT])
        return context

# class PostImagesListView(generic.ListView):
#     model = PostImages
#     def get_queryset(self):
#         return PostImages.objects.filter(post=self.request.post).order_by('order')


class PostDetailView(generic.DetailView):
    model = Post


class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        vip = UserExtends.objects.get(user=self.request.user).vip
        kwargs['vip'] = vip 
        if vip < timezone.now(): 
            kwargs['maxsymb'] = USEXT_TEXT_LENGTH_COMMON
        else:
            kwargs['maxsymb'] = USEXT_TEXT_LENGTH_VIP
        return kwargs

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        vip = UserExtends.objects.get(user=self.request.user).vip
        if vip < timezone.now():
            post_form = PostImagesFormSet()
        else:
            post_form = PostImagesFormSetVip()
        # post_form = PostImagesFormSet()
        return self.render_to_response(self.get_context_data(form=form,post_form=post_form))       

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        # print('*'*60)
        vip = UserExtends.objects.get(user=self.request.user).vip
        # print(vip)
        # print('*'*60)
        if vip < timezone.now():
            post_form = PostImagesFormSet(self.request.POST, self.request.FILES)
        else:
            post_form = PostImagesFormSetVip(self.request.POST, self.request.FILES)
        # post_form = PostImagesFormSet(self.request.POST, self.request.FILES)
        if (form.is_valid() and post_form.is_valid()):
            return self.form_valid(form, post_form)
        return self.render_to_response(self.get_context_data(form=form,post_form=post_form))       

    def form_valid(self, form, post_form):
        form.instance.user = self.request.user
        self.object = form.save()
        post_form.instance = self.object
        post_form.save()
        return redirect(self.success_url)



def user_permitted(function): 
    def _wrapped_view(request, *args, **kwargs): 
        obj = Post.objects.get(id = kwargs['pk'])
        if obj.user != request.user: 
            return redirect(reverse_lazy('perm-denied')) 
        return function(request, *args, **kwargs) 
    return _wrapped_view 



class PostUpdate(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        vip = UserExtends.objects.get(user=self.request.user).vip
        kwargs['vip'] = vip 
        if vip < timezone.now(): 
            kwargs['maxsymb'] = USEXT_TEXT_LENGTH_COMMON
        else:
            kwargs['maxsymb'] = USEXT_TEXT_LENGTH_VIP
        return kwargs

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        vip = UserExtends.objects.get(user=self.request.user).vip
        if vip < timezone.now():
            post_form = PostImagesFormSet(instance = self.object)
        else:
            post_form = PostImagesFormSetVip(instance = self.object)
        return self.render_to_response(self.get_context_data(form=form,post_form=post_form))       

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        vip = UserExtends.objects.get(user=self.request.user).vip
        if vip < timezone.now():
            post_form = PostImagesFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            post_form = PostImagesFormSetVip(self.request.POST, self.request.FILES, instance=self.object)
        # post_form = PostImagesFormSet(self.request.POST, self.request.FILES, instance=self.object)
        if (form.is_valid() and post_form.is_valid()):
            return self.form_valid(form, post_form)
        return self.render_to_response(self.get_context_data(form=form,post_form=post_form))       

    def form_valid(self, form, post_form):
        self.object = form.save()
        post_form.instance = self.object
        # print('41'*30)
        post_form.save()
        return redirect(self.success_url)    



class PostDelete(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('posts')
    # def get_queryset(self):
    #     base_queryset = super(PostUpdate, self).get_queryset()
    #     return base_queryset.filter(user = self.request.user)
import account.forms
import account.views
from django.views import View
from usext.models import UserExtends
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import render,render_to_response
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib.auth.decorators import login_required

class LoginView(account.views.LoginView):
    form_class = account.forms.LoginEmailForm

class SignupView(account.views.SignupView):

	def after_signup(self, form):
		usext = UserExtends()
		usext.user = User.objects.get(id = self.created_user.id)
		usext.vip = timezone.now()
		usext.save()

@login_required
def ContactView(request):
    form = ContactForm()
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail('socio', cd['message'], cd.get('email', 'noreply@example.com'), ['my@mail.ru'],)
        # else:
        # 	# cd = form.cleaned_data
        # 	# form.message = cd.get('message')
        # 	data = {'message':'mdsfa fas dfadf d essage','email':'mdsfa fas dfadf d essage','name':'mdsfa fas dfadf d essage',}
        # 	# print('i'*60)
        # 	# print(cd.get('message'))
        # 	form = ContactForm(request.POST, initial=data)
            # return HttpResponseRedirect('/contact/thanks/')
    # else:
    #     form = ContactForm()
        # return render(request, 'contacts.html', context={'contact_form':form},)

    # return render_to_response('contact.html', {'form': form}, context_instance=RequestContext(request))


    return render(request, 'contacts.html', context={'contact_form':form},)

def agree(request):
	return render(request,'agree.html')
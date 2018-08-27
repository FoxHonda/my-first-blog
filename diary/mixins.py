from django.shortcuts import redirect


class LogoutRequiredMixin:

    logout_url = str()


    def dispatch(self, request, *args, **kwargs):

        if request.user and request.user.is_authenticated:

            return redirect(self.logout_url)

        return super(LogoutRequiredMixin, self).dispatch(request, *args, **kwargs)

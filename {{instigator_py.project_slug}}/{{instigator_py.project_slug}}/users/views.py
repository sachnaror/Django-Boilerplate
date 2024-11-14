import environ
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
{%- if instigator_py.use_drf == "y" %}
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
{%- endif %}

env = environ.Env()
User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    {%- if instigator_py.username_type == "email" %}
    slug_field = "id"
    slug_url_kwarg = "id"
    {%- else %}
    slug_field = "username"
    slug_url_kwarg = "username"
    {%- endif %}


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert self.request.user.is_authenticated  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        {%- if instigator_py.username_type == "email" %}
        return reverse("users:detail", kwargs={"pk": self.request.user.pk})
        {%- else %}
        return reverse("users:detail", kwargs={"username": self.request.user.username})
        {%- endif %}


user_redirect_view = UserRedirectView.as_view()


{%- if instigator_py.use_drf == "y" %}
class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    client_class = OAuth2Client
    callback_url = env("FACEBOOK_CALLBACK_URL")


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = env("GOOGLE_CALLBACK_URL")
    client_class = OAuth2Client
{%- endif %}

from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    succes_url = reverse_lazy("login")
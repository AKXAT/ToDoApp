from django.urls import reverse_lazy
from .models import Task
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView 
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Login(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True 

    def get_success_url(self) -> str:
        return reverse_lazy('tasklist')


class TaskList(LoginRequiredMixin , ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        return context
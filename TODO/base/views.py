from django.urls import reverse_lazy
from .models import Task
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView 
from django.contrib.auth.mixins import LoginRequiredMixin

# Creating Class based views
#  
class Login(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True 

    def get_success_url(self) -> str:
        return reverse_lazy('tasklist') # if the user auth is success he/she should be directed to the task list 


class TaskList(LoginRequiredMixin , ListView): #Login required mixin is a restriction added for users to login before they can view thier list
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs): #only the auth user can see their respective items
        context =  super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user) #updating the context object to just view the respective user data
        return context
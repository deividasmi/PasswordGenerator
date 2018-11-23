

# def home(request):
#     return HttpResponse('Its works!')

from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
#from django.contrib.auth.models import User

from home.forms import HomeForm, ModifyPassword,CreatePinForm, PasswordCreationForm
from home.models import Post, Password
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm

class HomeView(TemplateView):
    template_name = 'home/home.html'


    def get(self, request):
        form = HomeForm()
        passwords = Password.objects.all()
        args = {
            'form': form, 'passwords': passwords
        }
        return render(request, self.template_name, args)


    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('home:home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

def passwords(request):
    if request.method == 'POST':
        form = ModifyPassword(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('home:home'))
    else:
        form = ModifyPassword(instance=request.user)
        args = {'form': form}
        return render(request, 'home/modify_passwords.html', args)


def password_delete(request, password_id=None):
        object = Password.objects.get(id=password_id)
        object.delete()
        return redirect(reverse('home:home'))
        #return render(request, 'ur template where you want to redirect')




class CreatePassword(TemplateView):

    template_name = 'home/create_new_password.html'

    def get(self, request):
        form = CreatePinForm()
        passwords = Password.objects.all()


        args = {
            'form': form, 'password': passwords
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = CreatePinForm(request.POST)
        if form.is_valid():
            password = form.save(commit=False)
            password.user = request.user
            password.save()

            text = form.cleaned_data['website']
            form = CreatePinForm()
            return redirect('home:home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

        #form = PasswordCreationForm()

   # args = {'form': form}
    #return render(request, 'home/create_new_password.html', args)

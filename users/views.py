from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from django.shortcuts import get_object_or_404


def hello(request):
    return HttpResponse("Hello, World!")


def user_list(request):
    users = User.objects.all()
    print(len(users))  # Debug output
    return render(request, 'users/user_list.html', {'users': users})



def new_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'users/new_user.html', {'form': form})


def user_detail(request, id):
    user = User.objects.get(id=id)
    return render(request, 'users/user_detail.html', {'user': user})


def user_detail(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'users/user_detail.html', {'user': user})
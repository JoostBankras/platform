from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, 'Your account has been created! You are now allowed to Log In!'.format())
            return redirect("login")
    else:
        form = UserRegisterForm(request.POST)
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile is updated'.format())
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form' : u_form,
        'p_form': p_form,
    }

    return render(request,"users/profile.html",context)

@login_required
def user_profile(request, username=None):
    if username:
        user = User.objects.get(username=username)
        context = {
        'user' : user
    }
        return render(request,"users/user_profile.html", context)
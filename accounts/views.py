from django.contrib.auth.decorators import login_required
from .forms import UserEditForm, ProfileEditForm, UserRegistrationForm
from django.shortcuts import render
from .models import Profile
from django.contrib.auth.forms import UserCreationForm



# def register(request):
#     if request.method == "POST":
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(user_form.cleaned_data["password"])
#             new_user.save()
#             Profile.objects.create(user=new_user)
#             return render(request, "account/register_done.htm", {"new_user": new_user})

#     else:
#         user_form = UserRegistrationForm()
#     return render(request, "account/register.htm", {"user_form": user_form})

def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        register_form = UserRegistrationForm(request.POST)
        if user_form.is_valid() and register_form.is_valid():
            user = user_form.save()
            register = register_form.save(commit=False)
            register.user = user
            register.save()
            return redirect('myquora:home')
    else:
        user_form = UserCreationForm()
        register_form = UserRegistrationForm()
    return render(request,'account/register.htm',{'user_form': user_form, 'register_form':UserRegistrationForm})
@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(
        request,
        "account/dashboard.htm",
        {"user_form": user_form, "profile_form": profile_form},
    )



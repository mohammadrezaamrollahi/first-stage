from .forms import UserRegisterForm, UserEditForm
from django.views.generic import CreateView,UpdateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




class register(CreateView):
    form_class = UserRegisterForm
    template_name = "account/register.htm"
    success_url = reverse_lazy("account:login")


class UserEditView(LoginRequiredMixin,UpdateView):
    form_class = UserEditForm 
    template_name = "account/edit_profile.htm"
    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user

class UserProfileView(LoginRequiredMixin,TemplateView):
    template_name = "account/profile.htm"








# from django.contrib.auth.decorators import login_required
# from .forms import UserEditForm, ProfileEditForm
# from django.shortcuts import render
# from .models import Profile
# from django.contrib.auth.forms import UserCreationForm
# from django.views.generic import CreateView
# from django.urls import reverse_lazy


# class register(CreateView):
#     form_class = UserCreationForm
#     template_name = "account/register.htm"
#     success_url = reverse_lazy("account:dashboard")



# # def register(request):
# #     if request.method == "POST":
# #         user_form = UserRegistrationForm(request.POST)
# #         if user_form.is_valid():
# #             new_user = user_form.save(commit=False)
# #             new_user.set_password(user_form.cleaned_data["password"])
# #             new_user.save()
# #             Profile.objects.create(user=new_user)
# #             return render(request, "account/register_done.htm", {"new_user": new_user})

# #     else:
# #         user_form = UserRegistrationForm()
# #     return render(request, "account/register.htm", {"user_form": user_form})

# # def register(request):
# #     if request.method == 'POST':
# #         user_form = UserCreationForm(request.POST)
# #         register_form = UserRegistrationForm(request.POST)
# #         if user_form.is_valid() and register_form.is_valid():
# #             user = user_form.save()
# #             register = register_form.save(commit=False)
# #             register.user = user
# #             register.save()
# #             return redirect('myquora:home')
# #     else:
# #         user_form = UserCreationForm()
# #         register_form = UserRegistrationForm()
# #     return render(request,'account/register.htm',{'user_form': user_form, 'register_form':UserRegistrationForm})
# @login_required
# def edit(request):
#     if request.method == "POST":
#         user_form = UserEditForm(instance=request.user, data=request.POST)
#         profile_form = ProfileEditForm(
#             instance=request.user.profile, data=request.POST, files=request.FILES
#         )

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#     else:
#         user_form = UserEditForm(instance=request.user)
#         profile_form = ProfileEditForm(instance=request.user.profile)
#     return render(
#         request,
#         "account/dashboard.htm",
#         {"user_form": user_form, "profile_form": profile_form},
#     )



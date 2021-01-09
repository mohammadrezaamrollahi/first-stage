from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserEditForm(UserChangeForm):

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]








# from django import forms
# from django.contrib.auth.models import User
# from .models import Profile
# from django.contrib.auth.forms import UserCreationForm

# class UserCreationForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields =("username","password1", "password2",)

# # class UserRegistrationForm(forms.ModelForm):
# #     password = forms.CharField(label="Password", widget=forms.PasswordInput)
# #     password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

# #     class Meta:
# #         model = User
# #         fields = ("username", "first_name", "email",)

# #     def clean_password2(self):
# #         cd = self.cleaned_data
# #         if cd["password"] != cd["password2"]:
# #             raise forms.ValidationError("Passwords don't match.")
# #         return cd["password2"]


# class UserEditForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ["email",]


# class ProfileEditForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ["gender", "interests", "avatar",]
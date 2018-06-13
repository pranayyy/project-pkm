from django.shortcuts import HttpResponse
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User,Setupuser,Buildkb
from django.forms import ModelForm
from django.db.models import Q
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('email','username','phone_number')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = UserChangeForm.Meta.fields



class Set_User_Form(ModelForm):

    share_KB_with = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)
    def __init__(self, *args, **kwargs):
        current_user = kwargs.pop('user', None)
        super(Set_User_Form, self).__init__(*args, **kwargs)
        if current_user is not None:
        # Modify the queryset here as you see fit
             self.fields['share_KB_with'].queryset = User.objects.all().filter(~Q(email__iexact=current_user.email))

    class Meta:
        model=Setupuser
        exclude=["email_id"]


class Build_kbform(ModelForm):

     knowledge = forms.Textarea()
     share_with = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple,required=False)
     def __init__(self, *args, **kwargs):
         current_user = kwargs.pop('user', None)
         super(Build_kbform, self).__init__(*args, **kwargs)

         if current_user is not None:
             # Modify the queryset here as you see fit
             self.fields['share_with'].queryset = User.objects.filter(id__in=Setupuser.share_KB_with.through.objects.values_list("user_id").filter(setupuser_id=Setupuser.objects.values_list("id",flat=True).filter(email_id=current_user.email)[0]))
     class Meta:
        model=Buildkb
        exclude=["email","keywords"]

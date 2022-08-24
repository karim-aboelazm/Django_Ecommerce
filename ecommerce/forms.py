from django import forms
from .models import *

class SubscribeForm(forms.ModelForm):
   class Meta:
        model = Subscriber
        fields = ['email']

class ClientRegisterForm(forms.ModelForm):
   username = forms.CharField(widget=forms.TextInput())
   email = forms.CharField(widget=forms.EmailInput())
   password = forms.CharField(widget=forms.PasswordInput())
   class Meta:
        model = Clients
        fields = ['username','full_name','email','password','address']
   
   def clean_username(self):
         user_name = self.cleaned_data['username'] 
         qs = User.objects.filter(username=user_name)
         if qs.exists():
               raise forms.ValidationError("Client with this username already exists.")
         return user_name

class ClientLoginForm(forms.Form):
      username = forms.CharField(widget=forms.TextInput())
      password = forms.CharField(widget=forms.PasswordInput())
      def clean_username(self):
            user_name = self.cleaned_data['username'] 
            qs = User.objects.filter(username=user_name)
            if not qs.exists():
                  raise forms.ValidationError("Client with this username does not exist.")
            return user_name


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['full_name','address','image','phone_number']


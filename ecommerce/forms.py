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

class ForgotPasswordForm(forms.Form):
      email = forms.CharField(widget=forms.EmailInput(
            attrs={'class':"form-control",
            'placeholder':"Enter your email here .."}
      ))
      def clean_email(self):
            email = self.cleaned_data.get('email')
            qs = Clients.objects.filter(user__email=email)
            if not qs.exists():
                  raise forms.ValidationError("Email does not exist.")
            return email

class PasswordResetForm(forms.Form):
      new_password = forms.CharField(widget=forms.PasswordInput(
            attrs={'class':"form-control",
            'autocomplete':"new-password",
            'placeholder':"Enter your Password here .."}
      ),label="New Password")

      confirm_password = forms.CharField(widget=forms.PasswordInput( 
            attrs={'class':"form-control",
            'autocomplete':"confirm-password",
            'placeholder':"Confirm your Password here .."}
      ),label="Confirm New Password")

      def clean_confirm_new_password(self):
            new_password = self.cleaned_data.get('new_password')
            confirm_password = self.cleaned_data.get('confirm_password')
            if new_password != confirm_password:
                  raise forms.ValidationError("Password does not match.")
            return confirm_password
      
class CheckoutForm(forms.ModelForm):
      class Meta:
            model = Order
            fields = ['client','shipping_address','phone','email','payment_method']
from django import forms
from .models import Reg



class RegForm(forms.Form):
    Username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your Username","id":"form_name"}))
    Fullname=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your FullName","id":"form_name"}))
    Email=forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your Email","id":"form_name"}))
    Password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password","id":"form_name"}))
    

class LoginForm(forms.Form):
    

    Username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter username","id":"form_name"}))
    Password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password","id":"form_name"}))


class ForgetForm(forms.Form):
    

    Email=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Email","id":"form_name"}))




from django import forms
from.models import User,Agent,Attraction
from django.forms.widgets import NumberInput

class Userdb(forms.ModelForm):
    class Meta:
        model = User
        fields = (
           'username','email','password','dob','address'
        )

class UserForm(forms.Form):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': 'form-control bg-transparent ', 'placeholder': 'Enter your name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control bg-transparent', 'placeholder': 'Enter email'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control bg-transparent', 'placeholder': 'Enter password'}))
    dob = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    address = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'class': 'form-control bg-transparent', 'placeholder': 'Enter Address'}))

class UserloginForm(forms.Form):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': 'form-control bg-transparent ', 'placeholder': 'Enter your name'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control bg-transparent', 'placeholder': 'Enter password'}))

class AgentloginForm(forms.Form):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': 'form-control bg-transparent ', 'placeholder': 'Enter your name'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control bg-transparent', 'placeholder': 'Enter password'}))

class Agentdb(forms.ModelForm):
    class Meta:
        model=Agent
        fields=(
            'username','agency_name','email_id','password','gst_no','upi_id','agency_logo','about_us'
        )

class AgentForm(forms.Form):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': 'form-control bg-transparent custom-placeholder', 'placeholder': 'Enter your Name'}))
    agency_name  = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': 'form-control bg-transparent', 'placeholder': 'Enter Agency Name'}))
    email_id = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control bg-transparent', 'placeholder': 'Enter Email'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control bg-transparent', 'placeholder': 'Create password'}))
    gst_no = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control bg-transparent', 'placeholder': 'Enter correct GST number'}))
    upi_id = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class': 'form-control bg-transparent', 'placeholder': 'Enter UPI ID'}))
    agency_logo = forms.ImageField()
    about_us = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control bg-transparent', 'placeholder': 'Tell something about your agency'})
    )

# class Attractiondb(forms.ModelForm):
#     class Meta:
#         model = Attraction
#     fields=(
#         'name','att_img'
#     )

# class AttractionForm(forms.Form):
#     name = forms.CharField(max_length=90,widget=forms.TextInput(attrs={'class': 'form-control bg-transparent custom-placeholder', 'placeholder': 'Enter your Name'}))
#     att_img = forms.ImageField()



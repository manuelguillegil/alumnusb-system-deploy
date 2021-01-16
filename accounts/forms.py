from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import User_information
from django.contrib.auth.views import LoginView

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', 
        max_length=152,
        required=True, 
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Username', 'style': 'background-color: rgba(73, 80, 87, 0.1)'}),
    )

    email = forms.CharField(
        label="Email",
        max_length=254, 
        required=True, 
        widget=forms.EmailInput(attrs={'class': "form-control", 'placeholder': 'info@example.com', 'style': 'background-color: rgba(73, 80, 87, 0.1)'}),
    )
    
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Password', 'style': 'background-color: rgba(73, 80, 87, 0.1)'}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label="Password Confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Password Confirmation', 'style': 'background-color: rgba(73, 80, 87, 0.1)'}),
        help_text="Enter the same password as before, for verification.",
    )
    #EL COLOR 69, 220, 53
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(LoginView):
    username = forms.CharField(
        label='Username',
        max_length=152,
        required=True, 
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': 'Username', 'style': 'background-color: rgba(73, 80, 87, 0.1)'}),
    )
    
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': 'Password', 'style': 'background-color: rgba(73, 80, 87, 0.1)'}),
    )

    class Meta:
        model = User
        fields = ('username', 'password')

class EditUserDataForm(forms.ModelForm):#UserChangeForm):
    """docstring for EditUserData"""
    #message = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = User_information
        fields = (
            'First_name',
            'Middle_name',
            'Last_name',
            'Mailing_city',
            'Mailing_state',
            'USB_alumn',
            #'Codigo_Alumn_USB',
            'Mailing_country',
            #'Email',
            'Mobile',
            'Cohorte',
            'Birthdate',
            'Age',
            'Undergrad_degree',
            'Graduate_degree',
            'Carnet',
            'USB_undergrad_campus',
            'Graduate_campus',
            'Work_email',
            'Workplace',
            'Donor',
            'Social_networks',
            'Twitter_account',
            'Instagram_account'
        )


class getUserDataForm(forms.ModelForm):#UserChangeForm):
    """docstring for EditUserData"""
    #message = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = User_information
        fields = (
            'First_name',
            'Middle_name',
            'Last_name',
            'Mailing_city',
            'Mailing_state',
            'USB_alumn',
            #'Codigo_Alumn_USB',
            'Mailing_country',
            #'Email',
            'Mobile',
            'Cohorte',
            'Birthdate',
            'Age',
            'Undergrad_degree',
            'Graduate_degree',
            'Carnet',
            'USB_undergrad_campus',
            'Graduate_campus',
            'Work_email',
            'Workplace',
            'Donor',
            'Social_networks',
            'Twitter_account',
            'Instagram_account'
        )
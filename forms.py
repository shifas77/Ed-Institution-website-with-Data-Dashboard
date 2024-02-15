
"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from app.models import student
from app.models import admin_login
from app.models import professionals
from app.models import student_stat
from app.models import Employee
from app.models import Higher_S
from app.models import Final_HS
from .models import UploadImage  
from app.models import course_selection
class EmployeeForm(forms.ModelForm): 
    class Meta: 
        model = Employee 
        fields = ['name', 'emp_image'] 

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class UserImageForm(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = UploadImage  
        # It includes all the fields of model  
        fields = '__all__'  

class studentform(forms.ModelForm):  
    class Meta:  
        model =student
        fields = "__all__"

class professionalform(forms.ModelForm):  
    class Meta:  
        model =  professionals 
        fields = "__all__"

class admin_loginform(forms.ModelForm):  
    class Meta:  
        model =  admin_login
        fields = "__all__"

class UserImageForm(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = UploadImage  
        # It includes all the fields of model  
        fields = '__all__'  


class student_stat(forms.ModelForm):  
    class Meta:  
        model =student_stat
        fields = "__all__"



class HigherEDform(forms.ModelForm):  
    class Meta:  
        model =Higher_S
        fields = "__all__"


class FinalHSform(forms.ModelForm):  
    class Meta:  
        model =Final_HS
        fields = "__all__"


class CSelectionform(forms.ModelForm):  
    class Meta:  
        model =course_selection
        fields = "__all__"

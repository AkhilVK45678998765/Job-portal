from django import forms
from django.contrib.auth.models import User


class regform(forms.Form):
    companyname = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(max_length=30)
    password2 = forms.CharField(max_length=30)
    mobile = forms.IntegerField()
    address = forms.CharField(max_length=100)


class logform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=30)


class vaccancyuploadform(forms.Form):
    companyname = forms.CharField(max_length=30)
    email = forms.EmailField()
    jobtitle = forms.CharField(max_length=30)
    jobtype = forms.CharField(max_length=30)
    worktype = forms.CharField(max_length=30)
    experiencerequired = forms.CharField(max_length=30)
    qualificationrequired = forms.CharField(max_length=30)


class userregistrationform(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class userloginform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=50)


class userdetailsform(forms.Form):
    fullname = forms.CharField(max_length=30)
    email = forms.EmailField()
    resume = forms.FileField()
    image = forms.FileField()
    educationalqualification = forms.CharField(max_length=30)
    experience = forms.CharField(max_length=30)
    address = forms.CharField(max_length=200)
    mobile = forms.IntegerField()


class jobapplyform(forms.Form):
    companyname = forms.CharField(max_length=30)
    jobtitle = forms.CharField(max_length=30)
    fullname = forms.CharField(max_length=30)
    email = forms.EmailField()
    resume = forms.FileField()


class emailform(forms.Form):
    email = forms.EmailField()
    message = forms.CharField(max_length=100)

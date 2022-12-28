from django import forms
from django.core import validators
def check_for_a(value):
    if value[0].upper()=='A':
        raise forms.ValidationError('validation error statrs A')
def check_len(v):
    if len(v)<=5:
        raise forms.ValidationError('length error')
class NameForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a,validators.MaxLengthValidator(5)])
    father_name=forms.CharField(max_length=100,validators=[check_for_a])
    email=forms.EmailField()
    reemail=forms.EmailField()
    mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)

    #clean method
    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['reemail']
        if e!=r:
            raise forms.ValidationError('email is not matched')

    #clean_element method
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        
        if len(bot)>0:
            raise forms.ValidationError('bot is error')
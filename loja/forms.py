# criando os formularios com a classe forms do django 
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class":"form-control",
                "placeholder":"digite seu nome"
                }
            )
        )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class":"form-control",
                "placeholder":"digite seu email"
                }
            )
        )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                    "class": "form-control", 
                    "placeholder": "Digite sua mensagem"
                }
            )
        )
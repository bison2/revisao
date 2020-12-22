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

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("O Email deve ser do gmail.com")
        return email

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                    "class": "form-control", 
                    "placeholder": "digite seu nome de usuario"
                }
            )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                 "class": "form-control ", 
                 "placeholder": "Digite sua senha"
                }
            )
        )

class RegisterForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Digite seu nome completo'
            }
        )    
    )

    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs = {
                'class':'form-control',
                'placeholder':'digite um email válido'
            }
        )
    )

    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                'class':'form-control',
                'placeholder':'digite sua senha'
            }
        )
    )

    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                'class':'form-control',
                'placeholder':'confirme sua senha'
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('esse usuario ja existe. Tente outro')
        return username 

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('esse email ja existe, tente outro')
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2 :
            raise forms.ValidationError('as senhas devem ser iguais')
        return data
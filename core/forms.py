from core.models import AuthUserRegistration
from django import forms

__author__ = 'andrews'

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", required=True, max_length=30 ,widget=forms.TextInput(attrs={'class':"form-control"}))
    password = forms.CharField(label="Password", required=True, widget=forms.PasswordInput(attrs={'class':"form-control"}))

class DepositForm(forms.Form):

    user_id = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class':"mdb-select"}))
    amount = forms.DecimalField(required=True,widget=forms.NumberInput(attrs={'class':"form-control"}))

    def _populate_products_field(self):
        users = AuthUserRegistration.objects.all()
        choice_list = [(user.id, user.user) for user in users.order_by('created_at')]
        self.fields['user_id'].choices = choice_list

    def __init__(self,data=None,initial=None ):
        super(DepositForm, self).__init__(data=data, initial=initial)
        self._populate_products_field()


class GainForm(forms.Form):

    user_id = forms.ChoiceField(required=True, widget=forms.Select(attrs={'class':"mdb-select"}))
    amount = forms.DecimalField(required=True,widget=forms.NumberInput(attrs={'class':"form-control"}))

    def _populate_products_field(self):
        users = AuthUserRegistration.objects.all()
        choice_list = [(user.id, user.user) for user in users.order_by('created_at')]
        self.fields['user_id'].choices = choice_list

    def __init__(self,data=None,initial=None ):
        super(GainForm, self).__init__(data=data, initial=initial)
        self._populate_products_field()

class AmtForm(forms.Form):
    amt = forms.CharField()

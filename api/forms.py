from django import forms


class QueryForm(forms.Form):
    q = forms.CharField(max_length=100)

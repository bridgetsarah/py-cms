from django import forms

# new form class

class new_post(forms.Form):
    content = forms.CharField(max_lenght=256)
    created_at = forms.DateTimeField()

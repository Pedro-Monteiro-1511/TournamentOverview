from django import forms
from .models import Match

class MatchForm(forms.ModelForm):
     class Media:
        js = ('tournament/match_form.js',)
from django import forms

class transcriptForm(forms.Form):
    URL = forms.CharField(label='',  widget=forms.TextInput(attrs={'class':'url-input', 'placeholder': 'Enter the Youtube URL'}), max_length=100)
    lang = forms.ChoiceField(label='', choices=[('en','English'),('hi', 'Hindi')], widget=forms.Select(attrs={'class':'lang-input'}))
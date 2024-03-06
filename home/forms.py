from django import forms


class ConversionForm(forms.Form):
    convert_to = forms.ChoiceField(choices=[('Morse', 'Translate to Morse'), ('English', 'Translate to English'),], widget=forms.Select(attrs={'class': 'box dropdown-box'}), label='')
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'text', 'placeholder':'Enter Text'}), label='')

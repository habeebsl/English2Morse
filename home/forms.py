from django import forms


class ConversionForm(forms.Form):
    convert_to = forms.ChoiceField(choices=[('Morse', 'Morse'), ('English', 'English'),], widget=forms.Select(attrs={'class': 'box dropdown-box'}), label='')
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'text', 'placeholder':'Enter Text'}), label='')

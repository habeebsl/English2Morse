from django.shortcuts import render
from .forms import ConversionForm
from .utils import to_morse_code, to_english

# Create your views here.
def morse_code_conversion(request):
    form = ConversionForm(request.POST or None)
    convert = None
    if request.method == 'POST':
        if form.is_valid():
            convert_to = form.cleaned_data['convert_to']
            if convert_to == 'Morse':
                convert = to_morse_code(form.cleaned_data['text'])
            else:
                convert = to_english(form.cleaned_data['text'])
    return render(request, 'home.html', {'form':form, 'text':convert})
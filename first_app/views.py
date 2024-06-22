from django.shortcuts import render
from . forms import ExampleForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def DjangoForm(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = ExampleForm(request.POST)
    return render(request, 'django_form.html', {'form':form})
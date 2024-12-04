from django.shortcuts import render

# Create your views here.
def all_atom(request):
    return render(request, 'atomicapp/all_atom.html')
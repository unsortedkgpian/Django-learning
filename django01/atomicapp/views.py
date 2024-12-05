from django.shortcuts import render
from .models import DanjoVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def all_atom(request):
    backenddata = DanjoVarity.objects.all()
    return render(request, 'atomicapp/all_atom.html', {'atomsdata': backenddata})


def atom_details(request, atom_id):
    # backenddata = DanjoVarity.objects.all()
    atom = get_object_or_404(DanjoVarity, pk=atom_id)
    return render(request, 'atomicapp/atoms.html', {'atomdetails': atom})
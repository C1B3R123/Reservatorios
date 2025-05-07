from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required  # Proteção de rotas
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Reservoir  # Renomeado de "Reservatorio"
from .forms import ReservoirForm  # Renomeado de "ReservatorioForm"

@login_required
def list_reservoirs(request):
    query = request.GET.get('q', '')
    reservoirs = Reservoir.objects.filter(name__icontains=query) if query else Reservoir.objects.all()

    reservoirs_json = [
        {
            "name": r.name,
            "capacity": r.capacity,
            "current_level": r.current_level,
            "pump_status": r.pump_status,
            "latitude": r.latitude,
            "longitude": r.longitude,
        }
        for r in reservoirs
    ]

    return render(request, 'reservoir/list_reservoirs.html', {
        'reservoirs': reservoirs,
        'reservoirs_json': reservoirs_json,
        'query': query
    })

@csrf_exempt
@login_required
def add_reservoir(request):
    if request.method == 'POST':
        form = ReservoirForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_reservoirs')
    else:
        form = ReservoirForm()
    return render(request, 'reservoir/add_reservoir.html', {'form': form})

@login_required
def edit_reservoir(request, pk):
    reservoir = get_object_or_404(Reservoir, pk=pk)
    if request.method == 'POST':
        form = ReservoirForm(request.POST, instance=reservoir)
        if form.is_valid():
            form.save()
            return redirect('list_reservoirs')
    else:
        form = ReservoirForm(instance=reservoir)
    return render(request, 'reservoir/edit_reservoir.html', {'form': form, 'reservoir': reservoir})

def index(request):
    return render(request, 'reservoir/index.html')

@login_required
def delete_reservoir(request, pk):  
    reservoir = get_object_or_404(Reservoir, pk=pk)
    if request.method == 'POST':
        reservoir.delete()
        return redirect('list_reservoirs')
    return render(request, 'reservoir/delete_reservoir.html', {'reservoir': reservoir})

@login_required
def manage_reservoirs(request): 
    reservoirs = Reservoir.objects.all()
    return render(request, 'reservoir/manage_reservoirs.html', {'reservoirs': reservoirs})

@login_required
def reservoir_details(request, pk): 
    reservoir = get_object_or_404(Reservoir, pk=pk)
    return render(request, 'reservoir/details.html', {
        'reservoir': reservoir,
        'latitude': reservoir.latitude,
        'longitude': reservoir.longitude,
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faz login automático após o registro
            return redirect('index')  # Redireciona para a página inicial
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


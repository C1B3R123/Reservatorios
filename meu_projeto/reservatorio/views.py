from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Reservatorio
from .forms import ReservatorioForm

def listar_reservatorios(request):
    query = request.GET.get('q', '')  # Obtém o termo de busca
    reservatorios = Reservatorio.objects.filter(nome__icontains=query) if query else Reservatorio.objects.all()

    for reservatorio in reservatorios:
        reservatorio.altura_agua_calculada = (reservatorio.nivel_atual / reservatorio.capacidade) * 100 if reservatorio.capacidade > 0 else 0

    return render(request, 'reservatorio/listar_reservatorios.html', {'reservatorios': reservatorios, 'query': query})

@csrf_exempt
def adicionar_reservatorio(request):
    if request.method == 'POST':
        form = ReservatorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_reservatorios')
    else:
        form = ReservatorioForm()
    return render(request, 'reservatorio/adicionar_reservatorio.html', {'form': form})

def editar_reservatorio(request, pk):
    reservatorio = get_object_or_404(Reservatorio, pk=pk)
    if request.method == 'POST':
        form = ReservatorioForm(request.POST, instance=reservatorio)
        if form.is_valid():
            form.save()
            return redirect('listar_reservatorios')
    else:
        form = ReservatorioForm(instance=reservatorio)
    return render(request, 'reservatorio/editar_reservatorio.html', {'form': form, 'reservatorio': reservatorio})

def deletar_reservatorio(request, pk):
    reservatorio = get_object_or_404(Reservatorio, pk=pk)
    if request.method == 'POST':
        reservatorio.delete()
        return redirect('listar_reservatorios')
    return render(request, 'reservatorio/deletar_reservatorio.html', {'reservatorio': reservatorio})

def gerenciar_reservatorios(request):
    reservatorios = Reservatorio.objects.all()
    return render(request, 'reservatorio/gerenciar_reservatorios.html', {'reservatorios': reservatorios})

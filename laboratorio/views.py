from django.shortcuts import render, get_object_or_404, redirect
from .models import Laboratorio
from .forms import LaboratorioForm

def laboratorio_list(request):
    laboratorios = Laboratorio.objects.all()
    visit_count = request.session.get('visit_count', 0) + 1
    request.session['visit_count'] = visit_count

    return render(request, 'laboratorio_list.html', {'laboratorios': laboratorios, 'visit_count': visit_count})

def laboratorio_detail(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    return render(request, 'laboratorio_detail.html', {'laboratorio': laboratorio})

def laboratorio_create(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LaboratorioForm()
    return render(request, 'laboratorio_form.html', {'form': form})

def laboratorio_update(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'laboratorio_form.html', {'form': form})

def laboratorio_confirm_delete(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    return render(request, 'laboratorio_confirm_delete.html', {'laboratorio': laboratorio})

def laboratorio_delete(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)

    if request.method == 'POST':
        laboratorio.delete()
        return redirect('home')

    return render(request, 'laboratorio_confirm_delete.html', {'laboratorio': laboratorio})

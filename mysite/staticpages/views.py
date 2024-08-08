from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required
def home(request):
    return render(request, 'home.html')
from django.shortcuts import render, redirect
from .forms import RegistroDeUsoForm

def registro_uso_veiculo(request):
    if request.method == 'POST':
        form = RegistroDeUsoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redireciona para uma página de sucesso ou outra página
    else:
        form = RegistroDeUsoForm()
    return render(request, 'registro_uso_veiculo.html', {'form': form})

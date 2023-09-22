from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import modelform


# Create your views here.
class PaginaInicial(TemplateView):
    template_name = "index.html"

class Doe(TemplateView):
    template_name ="about-us.html"

class Servicos(TemplateView):
    template_name = "services.html"

class Blog(TemplateView):
    template_name = "blog.html"

class Contato(TemplateView):
    template_name = "contact-us.html"

def form_modelform(request):
    if request.method == 'POST':
        form = modelform(request.POST)
        if form.is_valid():
            form.save()  # Isso salva os dados no banco de dados
            return redirect('página_de_sucesso')  # Redirecione para uma página de sucesso após a doação ser salva
    else:
        form = modelform()

    return render(request, 'sua_template.html', {'form': form})
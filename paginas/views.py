from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import modelform
from django.views.generic import TemplateView


# Create your views here.
class PaginaInicial(TemplateView):
    template_name = "index.html"

# views.py
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import modelform

class Doe(TemplateView):
    template_name = "about-us.html"

    def get(self, request, *args, **kwargs):
        return self.render_to_response({'form': modelform(), 'enviado_com_sucesso': False})

    def post(self, request, *args, **kwargs):
        form = modelform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('página_de_sucesso')
        return self.render_to_response({'form': form, 'enviado_com_sucesso': False})


def form_modelform(request):
    if request.method == 'POST':
        form = modelform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('página_de_sucesso')
    else:
        form = modelform()

    return render(request, 'about-us.html', {'form': form})


class Servicos(TemplateView):
    template_name = "services.html"

class Blog(TemplateView):
    template_name = "blog.html"

class Contato(TemplateView):
    template_name = "contact-us.html"

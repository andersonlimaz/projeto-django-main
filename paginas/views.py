from django.views.generic import TemplateView

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
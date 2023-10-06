from django.shortcuts import render,get_object_or_404, redirect
from reserva.models import Reserva,Stand
from django.views.generic import ListView,CreateView,DeleteView,DetailView, UpdateView,TemplateView
from reserva.form import ReservaForm
from django.urls import reverse_lazy
from django.contrib.messages import views


#VIEWS COM CBV

class index(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_reservas'] = Reserva.objects.count()
        context['total_stands'] = Stand.objects.count()
        return context



class listReserva(ListView):
    template_name = 'core/listaReserva.html'
    model = Reserva
    context_object_name = 'reserva'
    paginate_by = 2



#criar
class Criar(views.SuccessMessageMixin,CreateView):

    form_class = ReservaForm
    template_name = 'core/formReserva.html'
    success_url = reverse_lazy('listar')
    success_message = "Reserva criada com sucesso!"


class Delete(views.SuccessMessageMixin,DeleteView):
    model = Reserva
    template_name = 'core/confirm.html'
    success_url = reverse_lazy("listar")
    context_object_name= "reserva"
    success_message = "Reserva deletada com sucesso!"




class ReservaUpdateView(views.SuccessMessageMixin,UpdateView):
  model = Reserva
  form_class = ReservaForm
  success_url = reverse_lazy("listar")
  template_name = "core/formReserva.html"
  success_message = "Reserva atualizada com sucesso!"


class ReservaDetalhe(DetailView):
    model = Reserva
    template_name = "core/detalheReserva.html"

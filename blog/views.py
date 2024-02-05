from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Items
import segno
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



class ItemsListView(ListView):
    model = Items
    template_name = 'home.html'
    context_object_name = 'items_list'

class ItemsDetailView(DetailView):
    model = Items
    template_name = 'detail.html'
    context_object_name = 'item'

class ItemsUpdateView(LoginRequiredMixin, UpdateView):
    model = Items
    template_name = 'update.html'
    context_object_name = 'item_update'
    fields = ['name', 'text', 'created_time', 'brand', 'audio','video', 'image', 'teacher']

class ItemsDeleteView(LoginRequiredMixin, DeleteView):
    model = Items
    template_name = 'delete.html'
    context_object_name = 'item_delete'
    fields = ['name', 'text', 'created_time', 'brand', 'audio','video', 'image', 'teacher']
    success_url = reverse_lazy('home')

class ItemsCreateView(LoginRequiredMixin, CreateView):
    model = Items
    template_name = 'create.html'
    context_object_name = 'item_create'
    fields = ['name', 'text', 'created_time', 'brand', 'audio','video', 'image', 'teacher']




def items_detail(request, pk):
    item = get_object_or_404(Items, pk=pk)

    qrcode = segno.make_qr(f"127.0.0.1:8000/{pk}")
    print(qrcode)
    qrcode.save(
        f"media/qr_codes/{pk}.png",
        scale=5,
        dark="darkblue",
    )
    qr_code_svg = qrcode.svg_data_uri(scale=5)
    print(qr_code_svg)
    context = {
        "item" : item,
        "qrcode" : qr_code_svg,
    }
    return render(request, 'detail.html',context)

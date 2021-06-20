
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from bookmark.models import Bookmark
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6
class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')










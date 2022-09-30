from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import AlbumForm
from webapp.models import AlbumModel


class AlbumView(ListView):
    model = AlbumModel
    template_name = 'album_temp/album_index.html'
    context_object_name = 'albums'
    ordering = '-created_at_album'


class DetailAlbum(DetailView):
    model = AlbumModel
    template_name = 'album_temp/detail_album_view.html'
    context_object_name = 'album'


class CreateAlbum(CreateView):
    template_name = 'album_temp/create_album.html'
    form_class = AlbumForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.album_author = user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("webapp:album_view")

class UpdateAlbum(UpdateView):
    model = AlbumModel
    template_name = 'album_temp/update_album.html'
    form_class = AlbumForm

    def get_success_url(self):
        return reverse("webapp:album_view")

class AlbumDelete(DeleteView):
    template_name = 'album_temp/album_delete.html'
    model = AlbumModel
    context_object_name = 'album'
    success_url = reverse_lazy('webapp:album_view')

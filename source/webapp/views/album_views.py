from django.views.generic import ListView, DetailView

from webapp.models import AlbumModel, ImagesModel


class AlbumView(ListView):
    model = AlbumModel
    template_name = 'album_temp/album_index.html'
    context_object_name = 'albums'
    ordering = '-created_at_album'

class DetailAldumView(DetailView):
    model = AlbumModel
    template_name = 'album_temp/detail_album_view.html'
    context_object_name = 'album'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['album'] = self.get_object()
        return context

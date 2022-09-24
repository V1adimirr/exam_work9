from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ImageForm
from webapp.models import ImagesModel


class IndexView(ListView):
    model = ImagesModel
    template_name = 'images_temp/index.html'
    context_object_name = 'images'
    ordering = '-created_at'


class ImageView(DetailView):
    model = ImagesModel
    template_name = 'images_temp/image_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image'] = self.get_object()
        return context


class ImageCreate(CreateView):
    template_name = 'images_temp/image_create.html'
    form_class = ImageForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("webapp:image_view", kwargs={"pk": self.object.pk})


class ImageUpdate(UpdateView):
    model = ImagesModel
    template_name = 'images_temp/image_update.html'
    form_class = ImageForm

    def get_success_url(self):
        return reverse('webapp:image_view', kwargs={'pk': self.object.pk})


class ImageDelete(DeleteView):
    template_name = 'images_temp/image_delete.html'
    model = ImagesModel
    context_object_name = 'image'
    success_url = reverse_lazy('webapp:index')

from django.urls import path

from webapp.views import IndexView, ImageView, ImageCreate, ImageUpdate, ImageDelete

app_name = "webapp"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('image/<int:pk>/', ImageView.as_view(), name='image_view'),
    path('create/', ImageCreate.as_view(), name='image_create'),
    path('update/<int:pk>/', ImageUpdate.as_view(), name='image_update'),
    path('delete/<int:pk>/', ImageDelete.as_view(), name='image_delete')
]
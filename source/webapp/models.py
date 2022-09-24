from django.contrib.auth import get_user_model
from django.db import models


class ImagesModel(models.Model):
    photo = models.ImageField(upload_to="images", verbose_name="Фотография")
    signature = models.CharField(max_length=50, verbose_name='Подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(get_user_model(), related_name='images_author',
                               on_delete=models.CASCADE, verbose_name='Автор')
    album = models.ForeignKey('webapp.AlbumModel', null=True, blank=True, related_name='images_album',
                              on_delete=models.CASCADE, verbose_name='Альбом')

    def __str__(self):
        return f"{self.signature}, {self.created_at}, {self.author}, {self.album}"

    class Meta:
        db_table = 'Images'
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class AlbumModel(models.Model):
    image_name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    album_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Автор альбома')
    created_at_album = models.DateTimeField(auto_now_add=True, verbose_name='Создание альбома')

    def __str__(self):
        return f"{self.image_name}, {self.description}, {self.album_author}, {self.created_at_album}"

    class Meta:
        db_table = 'Album'
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование')
    content = models.TextField(verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано?')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at', 'title']


class Category(models.Model):
    title = models.CharField(max_length=155, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

from django.db import models
from django.urls import reverse


# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=1, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'pk': self.pk})
        # return reverse('view_news', kwargs={'news_id': self.pk, })

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Категория', db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['title']

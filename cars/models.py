from django.db import models
from django.urls import reverse


class Cars(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    price = models.CharField(max_length=20, verbose_name="Цена", default="Цена не указана")
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Зап. Части'
        verbose_name_plural = 'Зап. части'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Orders(models.Model):
    title = models.CharField(max_length=150, verbose_name="Наименование")
    number = models.CharField(max_length=20, verbose_name="Номер телефона")
    order_status = models.BooleanField(default=False, verbose_name="Статус заказа")

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'
        ordering = ['title']
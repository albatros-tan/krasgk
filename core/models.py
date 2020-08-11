from django.db import models

from uuslug import slugify

# Create your models here.

class ServiceTable(models.Model):
    class Meta:
        verbose_name = "Сервисная таблица"
        verbose_name_plural = "Сервисных записей"
    label = models.CharField(default="New Note", max_length = 52)
    text = models.TextField()

    def __str__(self):
        return self.label


class Pages(models.Model):
    """Модель для хранения объектов сраниц"""
    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
        ordering = ['priority']
    priority = models.PositiveSmallIntegerField(default=1)
    title = models.CharField(max_length=255)
    header = models.CharField(max_length=255)
    slug = models.SlugField(verbose_name='URL', max_length=50, unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.header)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.header


class Articles(models.Model):
    """Модель для хранения текстов на странице"""
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
    header = models.CharField(max_length=155, blank=True, null=True,
        help_text='Опционально, когда для статьи необходимо выделить заголовок в отрыве от основной html разметки')
    text = models.TextField()
    page = models.ForeignKey('Pages', on_delete=models.CASCADE)


class Images(models.Model):
    """Изображения на странице"""
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
    label = models.CharField(max_length=155, blank=True, null=True,
        help_text='Опционально, подпись к изображению')
    image = models.ImageField(upload_to='img/%Y/%m/%d')
    page = models.ForeignKey('Pages', on_delete=models.CASCADE)


class Files(models.Model):
    """Обычные файлы на странице"""
    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
    label = models.CharField(max_length=155, blank=True, null=True,
        help_text='Опционально, подпись к файлу')
    file = models.ImageField(upload_to='files/%Y/%m/%d')
    page = models.ForeignKey('Pages', on_delete=models.CASCADE)

        

from django.db import models

from ckeditor.fields import RichTextField
from uuslug import slugify

# Create your models here.

class ServiceTable(models.Model):
    class Meta:
        verbose_name = "Сервисная таблица"
        verbose_name_plural = "Сервисные записи"
    label = models.CharField(default="New Note", max_length = 52)
    text = models.TextField()

    def __str__(self):
        return self.label


class Topic(models.Model):
    """Модель для редактирования кнопок меню"""
    class Meta:
        verbose_name = "Пункт"
        verbose_name_plural = "Пункты меню"
        ordering = ['priority', 'id']
    name = models.CharField(max_length=50,
        verbose_name='название пункта меню',
        help_text='текст, который вы видете в меню')
    priority = models.SmallIntegerField(default=10,
        verbose_name='приоритет',
        help_text='чем ниже число, тем ближе к левому краю будет кнопка')

    def __str__(self):
        return f"{self.name}"


class Pages(models.Model):
    """Модель для хранения объектов сраниц"""
    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
    title = models.CharField(max_length=255,
        help_text="Текст во вкладке браузера")
    header = models.CharField(max_length=255,
        verbose_name="Заголовок страницы")
    name_in_menu = models.CharField(max_length=128, blank=True, null=True,
        verbose_name='Имя кнопки в меню',
        help_text="Имя кнопки, ведущей на страницу, в меню")
    slug = models.SlugField(max_length=120, unique=True, blank=True,
        verbose_name='URL', 
        help_text="url-адрес страницы, можно не заполнять - будет сгенерирован автоматически")
    topic = models.ForeignKey(Topic, blank=True, null=True,
        on_delete=models.CASCADE,
        verbose_name='Пункт меню',
        help_text='Выберите пункт меню, к которому прикреплена страница')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.header)
        if self.name_in_menu is None or len(self.name_in_menu) == 0:
            self.name_in_menu = self.header[:128]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.header} ({self.slug})"


class Articles(models.Model):
    """Модель для хранения текстов на странице"""
    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты'
    header = models.CharField(max_length=155, blank=True, null=True,
        verbose_name='Заголовок (Необязательное поле)',
        help_text='Опционально, когда для статьи необходимо выделить заголовок в отрыве от основной html разметки')
    text = RichTextField()
    page = models.ForeignKey('Pages', on_delete=models.CASCADE,
        verbose_name="Страница",
        help_text="Страница, на которой будет размещен текст")

    def __str__(self):
        return f"{self.page.header} - {self.header}"


class Albums(models.Model):
    '''Альбомы'''
    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
    label = models.CharField(max_length=255, blank=True, null=True,
        help_text='Название альбома')
    skin = models.ImageField(upload_to='img/%Y/%m/%d', help_text='Обложка')
    page = models.ForeignKey('Pages', on_delete=models.CASCADE,
        verbose_name="Страница",
        help_text="Страница, на которой будет размещен альбом")

    def __str__(self):
        return self.label


class Images(models.Model):
    """Изображения на странице"""
    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
    label = models.CharField(max_length=155, blank=True, null=True,
        verbose_name='Подпись к изображению',
        help_text='Опционально, подпись к изображению')
    image = models.ImageField(upload_to='img/%Y/%m/%d')
    album = models.ForeignKey('Albums', blank=True, null=True,
        on_delete=models.CASCADE,
        verbose_name='Альбом',
        help_text='Альбом, к которому будет прикреплено изображение')
    show_in_slider = models.BooleanField(default=False, verbose_name='отображать в слайдере')

    def __str__(self):
        return f"{self.album.label} - {self.label}"


class Files(models.Model):
    """Обычные файлы на странице"""
    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
    label = models.CharField(max_length=155, blank=True, null=True,
        verbose_name='Подпись к к файлу',
        help_text='Опционально, подпись к файлу')
    file = models.FileField(upload_to='files/%Y/%m/%d')
    page = models.ForeignKey('Pages', on_delete=models.CASCADE,
        verbose_name='Страница',
        help_text='Страница, к которой будет прикреплен файл')

    def __str__(self):
        return f"{self.page.header} - {self.label}"

        

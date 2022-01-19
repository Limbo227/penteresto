from django.db import models


# Create your models here.
# Create your models here.


class News(models.Model):
    title = models.CharField(verbose_name='Название', blank=True,
                             max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    teg = models.ForeignKey('Tags', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Пост'
        ordering = ['-created']

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-title']

    def __str__(self):
        return self.title

class Views(models.Model):
    title = models.CharField(max_length=20)
    views = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.views}'


class Likes(models.Model):
    title = models.CharField(max_length=20)
    likes = models.IntegerField(default=0)
    post = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.likes}'


class Comments(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    author_name = models.CharField('Имя автора', max_length=55)
    comment = models.TextField('Комментарий', max_length=255)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ['-comment']

    def __str__(self):
        return self.author_name


class Tags(models.Model):
    teg = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['-teg']



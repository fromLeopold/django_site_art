from django.contrib.auth.models import User
from django.db import models


class Entry(models.Model):
    title = models.CharField("Название", max_length=200)
    picture = models.ImageField("Арт-работа", upload_to='pictures/')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "арт-работа"
        verbose_name_plural = "арт-работы"


class Comment(models.Model):
    owner = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    text = models.TextField("Комментарий")
    entry = models.ForeignKey(Entry, verbose_name="Арт-работа", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.owner} - {self.entry}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        

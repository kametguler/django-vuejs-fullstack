from django.db import models

class Task(models.Model):
    class Meta:
        verbose_name = 'Görev'
        verbose_name_plural = 'Görevler'

    title = models.CharField(max_length=100, verbose_name='Başlık')
    description = models.CharField(max_length=1000, verbose_name='Açıklama')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')

    def __str__(self):
        return self.title
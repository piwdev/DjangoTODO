from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100, verbose_name='カテゴリー名')

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name='件名')
    description = models.TextField(verbose_name='説明', blank=True)
    start_date = models.DateField(verbose_name='期限_開始日')
    until_date = models.DateField(verbose_name='期限_終了日')
    done_at = models.DateField(verbose_name='完了日', null=True, blank=True)
    categories = models.ForeignKey(Categories, null=True, blank=True, on_delete=models.SET_NULL, related_name='tasks_categories')

    def __str__(self):
        return self.title

# todo/models.py

from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان کار")
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات")
    completed = models.BooleanField(default=False, verbose_name="انجام شده")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['completed', '-created_at']
        verbose_name = "کار"
        verbose_name_plural = "کارها"




        

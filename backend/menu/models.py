from django.db import models


class MenuItem(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=100)

    url = models.CharField(max_length=200)

    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE, null=True,
                               blank=True, related_name='children')

    named_url = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Название'
        verbose_name_plural = 'Названия'
        ordering = ['-name']

    def __str__(self) -> str:
        return self.name


from django.db import models

LANGUAGE_CHOICES = (
    ('python','python'),
)
STYLE_CHOICES = (
    ('friently','friently'),
)

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100 ,blank=True ,default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friently', max_length=100)

    class Meta:
        ordering = ['created']

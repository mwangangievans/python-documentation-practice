
from django.db import models
from django.contrib.auth.models import AbstractUser
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth import get_user_model
from pygments.styles import get_all_styles
from django.contrib.auth.models import User


User = get_user_model()

LANGUAGE_CHOICES = (
    ('python','python'),('java','java'),
)
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])




class Snippet(models.Model):
    owner = models.ForeignKey(User, related_name='snippets' , on_delete=models.CASCADE ,to_field="id", null=True)
    hightlited = models.TextField(max_length=140, default='SOME STRING')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100 ,blank=True ,default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    def save(self, *args , **kwargs ):
        """
        Use the pygments library to create a highlighted HTML representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title' : self.title} if self.title else {}
        formatter = HtmlFormatter(style = self.style , linenos = linenos ,
                                  full = True , **options)
        self.hightlited = highlight(self.code , lexer , formatter)
        super().save(*args ,**kwargs)


    class Meta:
        ordering = ['created']



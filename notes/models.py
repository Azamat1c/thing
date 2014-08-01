from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    date_begin = models.DateField('Дата замечания',)
    author = models.ForeignKey(User)
    text_note = models.TextField('Текст замечания')
    status = models.BooleanField('Статус', default=1)
    date_close = models.DateField('Дата закрытия',)
    user_close = models.ForeignKey(User)

class Comment(models.Model):
    date = models.DateField('Дата комментария',)
    author = models.ForeignKey(User)
    text_comment = models.TextField('Текст комментария')
    note = models.ForeignKey(Note)
    

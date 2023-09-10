from django.contrib import admin

from .question import Quiz
from .answer import Answer

admin.site.register(Quiz)
admin.site.register(Answer)
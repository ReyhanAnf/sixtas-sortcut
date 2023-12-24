from django.contrib import admin
from .models import Posts, Answers, Replies

# Register your models here.
admin.site.register(Posts)
admin.site.register(Answers)
admin.site.register(Replies)
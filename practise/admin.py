from django.contrib import admin
from .models import Subjects, TestLogs, TestScripts

# Register your models here.
admin.site.register(Subjects)
admin.site.register(TestLogs)
admin.site.register(TestScripts)

from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('firm', 'date_applied', 'salary', 'tem_resposta')
    list_filter = ('is_home', 'date_response')
    search_fields = ('firm', 'name')

    def tem_resposta(self, obj):
        return bool(obj.offer)
    tem_resposta.boolean = True

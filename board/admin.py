from django.contrib import admin

# Register your models here.
from board.models import Board


class BoardAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Board, BoardAdmin)


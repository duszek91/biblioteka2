from django.contrib import admin
from .models import Book

# Register your models here.
# admin.site.register(Film)

@admin.register(Book)
class FilmAdmin(admin.ModelAdmin):
    # fields = ["title","description", "year"]
    exclude = []
    list_filter = ('author', 'year', 'rate')

# Register your models here.

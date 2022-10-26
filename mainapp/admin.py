from django.contrib import admin
from mainapp.models import News


# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'photo')
#     list_display_links = ('id', 'title')
#     search_fields = ('title', 'content')
#     prepopulated_fields = {"id": ("title",)}



admin.site.register(News)

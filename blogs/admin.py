from django.contrib import admin
from .models import Category, Blog, SocialLink, Comment

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title', 'category', 'author', 'is_featured', 'status')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured', 'status')

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(SocialLink)
admin.site.register(Comment)

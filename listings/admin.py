from django.contrib import admin
from .models import Post, Category, Item
from django.utils.html import format_html
from embed_video.admin import AdminVideoMixin

# Register your models here.

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)

@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','is_active', 'is_selected')
    list_filter = ('is_selected','title')
    prepopulated_fields = {'slug': ('title',)}



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')
    list_filter = ('status','created','publish','author')
    search_fields = ('title','body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status','publish')

from django.contrib import admin
from .models import Category, Post, Comment

# Register your models here.
@admin.register(Category)
class Category(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

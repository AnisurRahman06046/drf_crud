from django.contrib import admin
from . models import Blogs
# Register your models here.
@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display=['id','title','content','author','created_at','updated_at']

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from blog.models import BlogCategory
from blog.models import Blog,Comment
# Register your models here.

#class BlogAdmin(admin.ModelAdmin):
class BlogAdmin(SummernoteModelAdmin):
  list_display=('title','category','created_at','publish')
  search_fields=('title', 'content')
  list_filter = ('category','publish')
  list_editable=('publish',)
  #list_per_page=1
  SummernoteModelAdmin=('content',)

admin.site.register(BlogCategory)
admin.site.register(Comment)
admin.site.register(Blog,BlogAdmin)



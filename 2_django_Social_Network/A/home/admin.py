from django.contrib import admin

# Register your models here.

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'updated' )
    search_fields= ('slug','body')
    list_filter = ('updated', )
    prepopulated_fields = {'slug':('body',)}
    raw_id_fields = ('user',)

# admin.site.register(Post, PostAdmin)
















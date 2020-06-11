from django.contrib import admin
from post import models 

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display =['title','creat_date','content']
	list_display_links = ['creat_date']
	list_filter = ['title' , 'creat_date']
	search_fields = ['title','content','creat_date']
	list_editable = ['title' , 'content']

	ordering = ['title']
	class Meta:
		model = models.post

admin.site.register(models.post,PostAdmin) 
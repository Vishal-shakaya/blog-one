from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.conf import settings
from django.utils import timezone
# Create your models here.

# def upload_location(instance, filename):
#     return "%s/%s" %(instance.pk, filename)

class post(models.Model):
    """Post model"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True ,blank=True)
    title = models.CharField(max_length=254)
    publish = models.DateField(null=True , blank=True)
    draft = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    image = models.FileField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    creat_date = models.DateTimeField(auto_now=False , auto_now_add=True)

    # define representation name of post 
    def __str__(self):
    	return self.title 
    	
    def get_absolute_url(self):
    	return reverse('Post:detail', kwargs={'pk':self.pk})

    
    def post_publish(self):
        self.publish = timezone.now()
        self.save()    


def create_slug(instance , new_slug=None):
     slug = slugify(instance.title)
     if new_slug is not None:
        slug = new_slug
     qs = post.objects.filter(slug=slug).order_by('-slug')
     exist = qs.exists()

     if exist:
        new_slug = "%s-%s" %(slug , qs.first().id)
        return create_slug(instance , new_slug=new_slug)
     return slug       

def pre_save_reciver(sender,instance , *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_reciver ,sender=post)        
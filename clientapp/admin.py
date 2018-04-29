from django.contrib import admin
from .models import GCRequest
from django.utils.html import format_html
# Register your models here.

class GCRequestAdmin(admin.ModelAdmin):
    list_display=('user','description','status','requested_on')
    readonly_fields=('user','description','requested_on','location','provided_image')
    exclude=('image','latitude','longitde')

    def has_add_permission(self,request):
        return False

    def provided_image(self,obj):
        url=obj.image.url
        return format_html('<a href="%s"><img src="%s" width=500></a>'%(url,url))

    def location(self,obj):
        return format_html('<a href="%s">Show location</a>'%
        ('https://www.google.com/maps/search/'+str(obj.latitude)+','+str(obj.longitde)))

admin.site.register(GCRequest,GCRequestAdmin)

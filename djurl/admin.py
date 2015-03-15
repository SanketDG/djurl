from django.contrib import admin
from djurl.models import Url
# Register your models here.


class UrlsAdmin(admin.ModelAdmin):
    list_display = ('short_id', 'httpurl', 'pub_date', 'count')
    ordering = ('-pub_date',)

# Register the Urls model with UrlsAdmin options
admin.site.register(Url, UrlsAdmin)

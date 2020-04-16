from django.contrib import admin
from .models import Record
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.


# class DB_Admin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.TextField: {'widget': TinyMCE()}
#     }
#  This class is for having the extra features on the textfields. For now I will leave it as it is.
class RecordAdmin(admin.ModelAdmin):
    list_display = ('ETR_id', 'date_processed', 'AGE', 'SEX')
    search_fields = ('ETR_id', 'SEX')


admin.site.register(Record, RecordAdmin)

admin.site.site_header = "Clasified DATABASE"
admin.site.index_title = "Clasified Administration"

from django.contrib import admin
from .models import *

admin.site.register(Scan)
admin.site.register(ScanResult)
admin.site.register(Target)
admin.site.register(PentestTool)
admin.site.register(Category)



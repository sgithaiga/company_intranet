from django.contrib import admin
from .models import Post, Vacancies, Applications, HrDocs

admin.site.site_header = 'NCWSC INTRANET ADMINISTRATION'
admin.site.register(Post)
admin.site.register(Vacancies)
admin.site.register(Applications)
admin.site.register(HrDocs)
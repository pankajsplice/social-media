from django.contrib import admin
from localmingle_app.models import Contact, Blog, Newsletter


class NewsletterAdmin(admin.ModelAdmin):

    list_display = ('id', 'email', 'created_on')


class ContactAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'email', 'message', 'created_on')


class BlogAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'user', 'published_date', 'created_on', 'updated_on')

admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Blog, BlogAdmin)

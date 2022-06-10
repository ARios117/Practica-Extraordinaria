from django.contrib import admin
from catalog.models import Author, Book, Comment, Vote


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('title', 'date', )}
    readonly_fields = ["slug", "score"]


admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(Comment)
admin.site.register(Vote)

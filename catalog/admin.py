from django.contrib import admin
from  .models import Author, Genre, Language, Book, BookInstance
'''
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
'''
admin.site.register(Genre)
admin.site.register(Language)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth',  'date_of_death')]

admin.site.register(Author, AuthorAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status','due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None,{
            'fields':('book','imprint','id')
        }),
        ('Availabliity 處境',{
            'fields':('status', 'due_back')
        }),
    )


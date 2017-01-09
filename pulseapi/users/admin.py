"""
Admin setings for EmailUser app
"""
from django.contrib import admin

from .models import EmailUser

class EmailUserAdmin(admin.ModelAdmin):
    """
    Show a list of entries a user has submitted in the EmailUser Admin app
    """
    fields = ('password', 'last_login', 'email', 'name', 'entries','favorites')
    readonly_fields = ('entries','favorites')
    def entries(self, instance):
        """
        Show all entries as a string of titles. In the future we should make them links.
        """
        print('entries instance')
        print(instance)
        return ", ".join([str(entry) for entry in instance.entries.all()])

    # def display_favorites(self, instance):
    #     """
    #     Show all favorite entires as a string of titles
    #     """
    #     print(instance)
    #     print('favorite')
    #     return ", ".join([str(entry) for entry in instance.entries.all()])
    # display_favorites.short_description = 'Favs'

admin.site.register(EmailUser, EmailUserAdmin)

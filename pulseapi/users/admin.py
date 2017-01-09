"""
Admin setings for EmailUser app
"""
from django.contrib import admin
from .models import EmailUser


class UserFavoritesInline(admin.TabularInline):
    """
    We need an inline widget before we can do anything
    with the user/entry favorite data.
    """
    model = EmailUser.favorites.through
    verbose_name = 'UserFavorites'


class EmailUserAdmin(admin.ModelAdmin):
    """
    Show a list of entries a user has submitted in the EmailUser Admin app
    """
    fields = ('password', 'last_login', 'email', 'name', 'entries','favorites')
    readonly_fields = ('entries','favorites')

    # this allows us to create/edit/delete/etc favorites:
    inlines = [ UserFavoritesInline ]

    def entries(self, instance):
        """
        Show all entries as a string of titles. In the future we should make them links.
        """
        print('entries instance')
        print(instance)
        return ", ".join([str(entry) for entry in instance.entries.all()])


admin.site.register(EmailUser, EmailUserAdmin)

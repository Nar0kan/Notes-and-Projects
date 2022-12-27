from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile

# Unregister Groups
admin.site.unregister(Group)

# Mix Profile into User info
class ProfileInline(admin.StackedInline):
    model = Profile

# Extend User model
class UserAdmin(admin.ModelAdmin):
    model = User

    # Users have only username fields on admin page
    fields = ["username"]
    inlines = [ProfileInline]

# Unregister initial User
admin.site.unregister(User)

# Register Users back with Profile
admin.site.register(User, UserAdmin)
#admin.site.register(Profile)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            "Profile",
            {
            "fields":("avatar","username","password","name","email","is_host","gender","language","currency",),
            "classes" : ("wide",),
            },
        ),
        ("Permissions", 
            {
            "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            "classes": ("collapse",),
            }
        ),
        (
            "Important Dates", 
            {
            "fields": ("last_login","date_joined"),
            "classes" : ("collapse",),
            },

            ),
        (
            "Coin",
            {
                "fields":("point",),

            }

        ),
    )
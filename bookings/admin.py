from django.contrib import admin
from .models import Booking
 # type: ignore
# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "kind",
        "user",
        "room",
        "experiences",
        "check_in",
        "check_out",
        "guests",
    )

    list_filter = (
        "kind",
    )
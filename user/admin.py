from django.contrib import admin
from orders.admin import AdminReservationInline
from user.models import User


# Register your models here.

#admin.site.register(User)




@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email"]
    search_fields = ["first_name", "last_name", "email"]

    inlines = [AdminReservationInline, ]



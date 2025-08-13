from django.contrib import admin

from orders.models import Reservation

#admin.site.register(Reservation)

@admin.register(Reservation)
class AdminReservation(admin.ModelAdmin):
    list_display = (
                    "quantity",
                    "phone",
                    "user_email",
                    "date",
                    "time",
                    "accepted",
                    "created_timestemp",
                    )
    search_fields = ["date", "time", "quantity",]
    fields = ["user", "user_fullname", "quantity", "phone", "date", "time", "accepted", "created_timestemp", "comment"]
    list_filter = ["quantity", "date", "time", "accepted"]
    readonly_fields = ("created_timestemp", "user_fullname")

    def user_email(self, obj):
        if obj.user.email:
            return str(obj.user.email)
    
    def user_fullname(self, obj):
        if obj.user.first_name and obj.user.last_name:
            return str(f'{obj.user.first_name} {obj.user.last_name}')
        else:
            return str("Нету имени и фамилии")

class AdminReservationInline(admin.TabularInline):
    model = Reservation
    fields = ["phone", "quantity", "date", "time", "accepted"]
    search_fields = ["time", "date", "quantity"]
    readonly_fields =  "created_timestemp",
    
    extra = 1
from django.contrib import admin

from products.models import Categories, Meals

# Register your models here.

#admin.site.register(Meals)
admin.site.register(Categories)


@admin.register(Meals)
class MealsAdmin(admin.ModelAdmin):
    list_display = ["name", "sell_price", "product_id"]
    search_fields = ["name",]
    list_filter = ["product_id", "price"]
    fields = [
        "name",
        "product_id",
        ("price", "discount"),
        "image",
    ]
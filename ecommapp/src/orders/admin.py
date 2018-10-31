from django.contrib import admin

from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_id","status", "total"]
    list_filter = ["status", "total"]
    list_display_links = ["order_id"]
    list_editable = ["status"]
    class Meta:
        model = Order

admin.site.register(Order,OrderAdmin)
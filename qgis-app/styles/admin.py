from django.contrib import admin

from .models import Review, Style, StyleType


class StyleTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "order")
    list_editable = ("order",)


class StyleAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "creator",
        "upload_date",
        "modified_date",
        "style_type",
    )
    search_fields = ("name", "description")


admin.site.register(Style, StyleAdmin)
admin.site.register(StyleType, StyleTypeAdmin)
admin.site.register(Review)

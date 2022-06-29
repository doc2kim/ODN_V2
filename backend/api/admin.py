from django.contrib import admin
from .models import Opendata

# Register your models here.


@admin.register(Opendata)
class OpendataAdmin(admin.ModelAdmin):
    """Opendata Admin Definition"""

    fieldsets = (
        ("Coordinates", {
            "fields": (
                "lat",
                "lng"
            )
        }),
        ("Location", {
            "fields": (
                "ocean",
                "area1",
                "area2",
                "area3",
                "area4"
            )
        }),
        ("State Info", {
            "fields": (
                "temp",
                "oxy",
                "ph",
                "salt",
                "ntu"
            )
        }),
        ("Time Info", {
            "fields": (
                "obs_date",
                "obs_time"
            )
        })
    )

    list_display = (
        "id",
        "ocean",
        "area1",
        "area2",
        "area3",
        "area4",
        "temp",
        "oxy",
        "ph",
        "salt",
        "ntu",
        "obs_date",
        "obs_time"
    )

    list_filter = (
        "ocean",
        "area1",
        "area2",
        "area3",
        "area4"
    )

    search_fields = ["ocean", "area1", "area2", "area3", "area4"]

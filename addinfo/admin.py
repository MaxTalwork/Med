from django.contrib import admin

from addinfo.models import ComText, Feedback


@admin.register(ComText)
class ComTextAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "surname",
        "contact_name",
        "patronymic",
        "avatar",
        "phone_number",
        "adress",
        "email",
        "mapurl",
        "map",
        "is_active",
    )
    list_filter = (
        "name",
        "description",
        "surname",
        "contact_name",
        "patronymic",
        "avatar",
        "phone_number",
        "adress",
        "email",
        "mapurl",
        "map",
        "is_active",
    )
    search_fields = (
        "name",
        "description",
        "surname",
        "contact_name",
        "patronymic",
        "avatar",
        "phone_number",
        "adress",
        "email",
        "mapurl",
        "map",
        "is_active",
    )


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "surname",
        "contact_name",
        "phone_number",
        "email",
    )
    list_filter = (
        "id",
        "title",
        "description",
        "surname",
        "contact_name",
        "phone_number",
        "email",
    )
    search_fields = (
        "id",
        "title",
        "description",
        "surname",
        "contact_name",
        "phone_number",
        "email",
    )

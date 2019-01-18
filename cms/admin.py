from django.contrib import admin
from .models import User, Day, Team

class UserAdmin(admin.ModelAdmin):
    list_display = ("roll", "name", "display_name", "created_at", "team_num",)

admin.site.register(User, UserAdmin)

class DayAdmin(admin.ModelAdmin):
    list_display = ("date", "emo",)

admin.site.register(Day, DayAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ("created_at", "users", "calendar",)

admin.site.register(Team, TeamAdmin)

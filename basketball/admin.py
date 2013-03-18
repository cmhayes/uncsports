#!/usr/bin/env python

from django.contrib import admin
from basketball.models import Team, Player

class TeamAdmin(admin.ModelAdmin):
	search_fields = ('name',)

admin.site.register(Team, TeamAdmin)

class PlayerAdmin(admin.ModelAdmin):
	search_fields = ('name',)

admin.site.register(Player, PlayerAdmin)
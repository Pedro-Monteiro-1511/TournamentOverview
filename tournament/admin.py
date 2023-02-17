from django.contrib import admin
from .models import Sport_Category, Tournament, Match, Team, TeamMember
from .forms import MatchForm

# Register your models here.
class MatchAdmin(admin.ModelAdmin):
    form = MatchForm

admin.site.register(Sport_Category)
admin.site.register(Tournament)
admin.site.register(Match, MatchAdmin)
admin.site.register(Team)
admin.site.register(TeamMember)




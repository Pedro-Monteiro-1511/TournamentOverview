from django.db import models
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Sport_Category(models.Model):
    designation = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.designation
    

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    tournament_type = ( 
        ('Individual', 'IND'),
        ('Team', 'TEAM')
    )
    type = models.CharField(max_length=10, choices=tournament_type, default='IND')
    date_start = models.DateTimeField()
    prize_pool = models.IntegerField(default=0)
    number_teams_participation = models.IntegerField(default=2)
    
    def __str__(self):
        return self.name
    


 
class Team(models.Model):
    team_name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, through='TeamMember')
    number_of_members = models.PositiveIntegerField(default=0)
    team_logo = models.ImageField(upload_to='team_logos/', null=True, blank=True)
    team_wins = models.PositiveIntegerField(default=0)
    team_losses = models.PositiveIntegerField(default=0)
    team_draws = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self):
        return self.team_name
    
    
class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    player1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_player1', blank=True, null=True)
    player2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches_player2', blank=True, null=True)
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_team1', blank=True, null=True)
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='matches_team2', blank=True, null=True)
    player1_points = models.PositiveIntegerField(blank=True, null=True)
    player2_points = models.PositiveIntegerField(blank=True, null=True)
    team1_points = models.PositiveIntegerField(blank=True, null=True)
    team2_points = models.PositiveIntegerField(blank=True, null=True)
    match_date = models.DateTimeField()
    
    def clean(self):
        matches = Match.objects.filter(
            tournament_id = self.tournament.id,
            match_date = self.match_date,
        )
        
        if matches.exists():
            raise ValidationError(('There is already a match scheduled at this time within this tournament. Please change accordingly'))
        
        
        if self.tournament.type == 'Individual':
            if self.player1 == self.player2:
                raise ValidationError('Player 1 and Player 2 cannot be the same.')
            if self.team1 or self.team2:
                raise ValidationError('Team fields should be left blank for Individual tournaments.')
            if not self.player1 or not self.player2:
                raise ValidationError('Both players should be specified for Individual tournaments.')
        elif self.tournament.type == 'Team':
            if self.team1 == self.team2:
                raise ValidationError('Team 1 and Team 2 cannot be the same.')
            if self.player1 or self.player2:
                raise ValidationError('Player fields should be left blank for Team tournaments.')
            if not self.team1 or not self.team2:
                raise ValidationError('Both teams should be specified for Team tournaments.')
        else:
            raise ValidationError('Invalid tournament type.')
        
        
        
        
            
    def save(self, *args, **kwargs):
        if self.tournament.type == 'Individual':
            self.team1 = None
            self.team2 = None
        elif self.tournament.type == 'Team':
            self.player1 = None
            self.player2 = None
        super().save(*args, **kwargs)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(player1_points__isnull=True) | models.Q(player2_points__isnull=True),
                name='players_points_null'
            ),
            models.CheckConstraint(
                check=models.Q(team1_points__isnull=True) | models.Q(team2_points__isnull=True),
                name='teams_points_null'
            ),
        ]

class TeamMember(models.Model):
    team = models.ForeignKey(Team,on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type_options = ( 
        ('MAN', 'Manager'),
        ('COACH', 'Coach'),
        ('P', 'Player'),
        ('CAP', 'Captain'),
    )
    type_of_member = models.CharField(max_length=10, choices= type_options, default='P')
    
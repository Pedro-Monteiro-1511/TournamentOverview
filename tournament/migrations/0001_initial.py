# Generated by Django 4.1.7 on 2023-02-15 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sport_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('number_of_members', models.PositiveIntegerField(default=0)),
                ('team_logo', models.ImageField(blank=True, null=True, upload_to='team_logos/')),
                ('team_wins', models.PositiveIntegerField(default=0)),
                ('team_losses', models.PositiveIntegerField(default=0)),
                ('team_draws', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Individual', 'IND'), ('Team', 'TEAM')], default='IND', max_length=10)),
                ('date_start', models.DateTimeField()),
                ('prize_pool', models.IntegerField(default=0)),
                ('number_teams_participation', models.IntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_member', models.CharField(choices=[('Manager', 'MAN'), ('Coach', 'COACH'), ('Player', 'P'), ('Capitain', 'CAP')], default='P', max_length=10)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(through='tournament.TeamMember', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1_points', models.PositiveIntegerField(blank=True, null=True)),
                ('player2_points', models.PositiveIntegerField(blank=True, null=True)),
                ('team1_points', models.PositiveIntegerField(blank=True, null=True)),
                ('team2_points', models.PositiveIntegerField(blank=True, null=True)),
                ('match_date', models.DateField(auto_now_add=True, null=True)),
                ('player1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches_player1', to=settings.AUTH_USER_MODEL)),
                ('player2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches_player2', to=settings.AUTH_USER_MODEL)),
                ('team1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches_team1', to='tournament.team')),
                ('team2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches_team2', to='tournament.team')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.tournament')),
            ],
        ),
        migrations.AddConstraint(
            model_name='match',
            constraint=models.CheckConstraint(check=models.Q(('player1_points__isnull', True), ('player2_points__isnull', True), _connector='OR'), name='players_points_null'),
        ),
        migrations.AddConstraint(
            model_name='match',
            constraint=models.CheckConstraint(check=models.Q(('team1_points__isnull', True), ('team2_points__isnull', True), _connector='OR'), name='teams_points_null'),
        ),
    ]

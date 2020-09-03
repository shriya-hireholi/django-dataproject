from django.db import models


# Create your models here.
class Deliveries(models.Model):
    delivery_id = models.IntegerField()
    inning = models.IntegerField()
    batting_team = models.CharField(max_length=50)
    bowling_team = models.CharField(max_length=50)
    over = models.IntegerField()
    ball = models.IntegerField()
    batsman = models.CharField(max_length=50)
    non_striker = models.CharField(max_length=50)
    bowler = models.CharField(max_length=50)
    is_super_over = models.IntegerField()
    wide_runs = models.IntegerField()
    bye_runs = models.IntegerField()
    legbye_runs = models.IntegerField()
    noball_runs = models.IntegerField()
    penalty_runs = models.IntegerField()
    batsman_runs = models.IntegerField()
    extra_runs = models.IntegerField()
    total_runs = models.IntegerField()
    player_dismissed = models.CharField(max_length=50)
    dismissal_kind = models.CharField(max_length=50)
    fielder = models.CharField(max_length=50)


class Matches(models.Model):
    match_id = models.IntegerField(primary_key=True)
    season = models.IntegerField()
    city = models.CharField(max_length=50)
    date = models.DateField()
    first_team = models.CharField(max_length=50)
    second_team = models.CharField(max_length=50)
    toss_winner = models.CharField(max_length=50)
    toss_decision = models.CharField(max_length=50)
    result = models.CharField(max_length=50)
    dl_applied = models.IntegerField()
    winner = models.CharField(max_length=50)
    win_by_runs = models.IntegerField()
    win_by_wickets = models.IntegerField()
    player_of_match = models.CharField(max_length=50)
    venue = models.CharField(max_length=150)
    umpire1 = models.CharField(max_length=50)
    umpire2 = models.CharField(max_length=50)
    umpire3 = models.CharField(max_length=50)

    def __str__(self):
        return self.batting_team


class Umpires(models.Model):
    umpire = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    first_officiated = models.IntegerField()
    last_officiated = models.IntegerField()
    no_of_matches = models.IntegerField()

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum, Count, Q
from .models import Deliveries, Matches, Umpires
from django.http import JsonResponse
import json


# Create your views here.
def base(request):
    teams = Deliveries.objects.values('batting_team').annotate(
        total_runs=Count('total_runs')
    ).order_by('batting_team')

    batsman_name = Deliveries.objects.values('batsman').filter(
        batting_team='Royal Challengers Bangalore').annotate(
        batsman_runs=Sum('batsman_runs')).order_by('-batsman_runs')[:11]

    ump_nation = Umpires.objects.values('nationality').exclude(
        nationality='India').annotate(
        umpires_count=Count('umpire'))

    seasons = Matches.objects.values(
        'season').distinct().order_by('season')

    return render(request, 'base.html', {
        'query_set': teams,
        'batsman_name': batsman_name,
        'ump_nation': ump_nation,
        'seasons': seasons})


@csrf_exempt
def total_runs_scored(request):
    json_data = json.loads(request.body)
    print(json_data)
    if len(json_data['teams']) == 0:
        for i in json_data['game']:
            if i == '7000':
                start = 0
                query_set = dict(Deliveries.objects.values_list(
                    'batting_team').annotate(total_runs=Count(
                        'total_runs')).filter(
                            total_runs__range=(start, 7000)).order_by(
                                    'batting_team'))
            elif i == '14000':
                print(4000)
                start = 7000
                query_set = dict(Deliveries.objects.values_list(
                    'batting_team').annotate(total_runs=Count(
                        'total_runs')).filter(
                            total_runs__range=(start, 14000)).order_by(
                                    'batting_team'))
            else:
                start = 14000
                query_set = dict(Deliveries.objects.values_list(
                    'batting_team').annotate(total_runs=Count(
                        'total_runs')).filter(
                            total_runs__range=(start, 19000)).order_by(
                                    'batting_team'))
        return JsonResponse(query_set, safe=False)
    elif json_data['game'] == ['']:
        query_set = dict(Deliveries.objects.values_list(
                    'batting_team').filter(
                        batting_team__in=json_data['teams']).annotate(
                            total_runs=Count('total_runs')).order_by(
                                    'batting_team'))
        
        return JsonResponse(query_set, safe=False)
    else:
        for i in json_data['game']:
            if i == '7000':
                start = 0
                query_set = dict(Deliveries.objects.values_list(
                    'batting_team').filter(
                        batting_team__in=json_data['teams']).annotate(
                            total_runs=Count('total_runs')).filter(
                            total_runs__range=(start, 7000)).order_by(
                                    'batting_team'))
            elif i == '3000':
                start = 1500
                query_set = dict(Deliveries.objects.values_list(
                    'batting_team').filter(
                        batting_team__in=json_data['teams']).annotate(
                            total_runs=Count('total_runs')).filter(
                            total_runs__range=(start, 14000)).order_by(
                                    'batting_team'))
            else:
                start = 3000
                query_set = dict(Deliveries.objects.values_list(
                    'batting_team').filter(
                        batting_team__in=json_data['teams']).annotate(
                            total_runs=Count('total_runs')).filter(
                            total_runs__range=(start, 19000)).order_by(
                                    'batting_team'))

        return JsonResponse(query_set, safe=False)


@csrf_exempt
def top_batsman_rcb(request):
    json_data = json.loads(request.body)
    print(json_data)
    if len(json_data['batsmans']) == 0:
        for i in json_data['run']:
            if i == '1500':
                start = 0
                query_set = dict(Deliveries.objects.values_list(
                    'batsman').filter(
                        batting_team='Royal Challengers Bangalore').annotate(
                            batsman_runs=Sum('batsman_runs')).filter(
                                batsman_runs__range=(start, 1500)).order_by(
                                    '-batsman_runs')[:11])
            elif i == '3000':
                start = 1500
                query_set = dict(Deliveries.objects.values_list(
                    'batsman').filter(
                        batting_team='Royal Challengers Bangalore').annotate(
                            batsman_runs=Sum('batsman_runs')).filter(
                                batsman_runs__range=(start, 3000)).order_by(
                                    '-batsman_runs')[:11])
            else:
                start = 3000
                query_set = dict(Deliveries.objects.values_list(
                    'batsman').filter(
                        batting_team='Royal Challengers Bangalore').annotate(
                            batsman_runs=Sum('batsman_runs')).filter(
                                batsman_runs__range=(start, 5000)).order_by(
                                    '-batsman_runs')[:11])

        return JsonResponse(query_set, safe=False)
    elif json_data['run'] == ['']:
        query_set = dict(Deliveries.objects.values_list(
                    'batsman').filter(
                        batting_team='Royal Challengers Bangalore').filter(
                            batsman__in=json_data['batsmans']).annotate(
                            batsman_runs=Sum('batsman_runs')).order_by(
                                    '-batsman_runs')[:11])

        return JsonResponse(query_set, safe=False)
    else:
        for i in json_data['run']:
            if i == '1500':
                start = 0
                query_set = dict(Deliveries.objects.values_list(
                    'batsman').filter(
                        batting_team='Royal Challengers Bangalore').filter(
                            batsman__in=json_data['batsmans']).annotate(
                            batsman_runs=Sum('batsman_runs')).filter(
                                batsman_runs__range=(start, 1500)).order_by(
                                    '-batsman_runs')[:11])
            elif i == '3000':
                start = 1500
                query_set = dict(Deliveries.objects.values_list(
                    'batsman').filter(
                        batting_team='Royal Challengers Bangalore').filter(
                            batsman__in=json_data['batsmans']).annotate(
                            batsman_runs=Sum('batsman_runs')).filter(
                                batsman_runs__range=(start, 3000)).order_by(
                                    '-batsman_runs')[:11])
            else:
                start = 3000
                query_set = dict(Deliveries.objects.values_list(
                    'batsman').filter(
                        batting_team='Royal Challengers Bangalore').filter(
                            batsman__in=json_data['batsmans']).annotate(
                            batsman_runs=Sum('batsman_runs')).filter(
                                batsman_runs__range=(start, 5000)).order_by(
                                    '-batsman_runs')[:11])

        return JsonResponse(query_set, safe=False)


@csrf_exempt
def foreign_umpire(request):
    json_data = json.loads(request.body)

    if len(json_data) > 0:
        query_set = dict(Umpires.objects.values_list('nationality').exclude(
            nationality='India').filter(nationality__in=json_data).annotate(
                umpires_count=Count('umpire')))
    else:
        query_set = dict(Umpires.objects.values_list('nationality').exclude(
            nationality='India').annotate(umpires_count=Count('umpire')))

    return JsonResponse(query_set, safe=False)


@csrf_exempt
def matches_team_season(request):
    json_data = json.loads(request.body)
    teams_season = {}
    teams_season_one = {}
    teams_season_two = {}
    if len(json_data['team']) == 0:
        query_set = list(Matches.objects.values(
            'season',
            'first_team',
            'second_team').filter(season__in=json_data['season']))
        for data in query_set:
            season = int(data['season'])
            team_one = data['first_team']
            team_two = data['second_team']

            if season not in teams_season:
                teams_season[season] = {}

            teams_season[season][team_one] = teams_season[season].get(
                team_one, 0)+1
            teams_season[season][team_two] = teams_season[season].get(
                team_two, 0)+1
        teams_season = dict(sorted(teams_season.items()))
    elif len(json_data['season']) == 0:
        query_set_first = list(Matches.objects.values(
            'season',
            'first_team').filter(first_team__in=json_data['team']))
        
        query_set_second = list(Matches.objects.values(
            'season',
            'second_team').filter(second_team__in=json_data['team']))
        
        for data in query_set_first:
            season = int(data['season'])
            team_one = data['first_team']

            if season not in teams_season_one:
                teams_season_one[season] = {}

            teams_season_one[season][team_one] = teams_season_one[season].get(
                team_one, 0)+1

        for data in query_set_second:
            season = int(data['season'])
            team_two = data['second_team']

            if season not in teams_season_two:
                teams_season_two[season] = {}

            teams_season_two[season][team_two] = teams_season_two[season].get(
                team_two, 0)+1

        for key in teams_season_one:
            if key in teams_season_two:
                for i in teams_season_one[key]:
                    if i in teams_season_two[key]:
                        teams_season_one[key][i] = teams_season_one[key][i] + teams_season_two[key][i]

        teams_season = dict(sorted(teams_season_one.items()))
    else:
        query_set_first = list(Matches.objects.values(
            'season',
            'first_team').filter(
                Q(season__in=json_data['season']) &
                Q(first_team__in=json_data['team'])))
        
        query_set_second = list(Matches.objects.values(
            'season',
            'second_team').filter(
                Q(season__in=json_data['season']) &
                Q(second_team__in=json_data['team'])))

        for data in query_set_first:
            season = int(data['season'])
            team_one = data['first_team']

            if season not in teams_season_one:
                teams_season_one[season] = {}

            teams_season_one[season][team_one] = teams_season_one[season].get(
                team_one, 0)+1

        for data in query_set_second:
            season = int(data['season'])
            team_two = data['second_team']

            if season not in teams_season_two:
                teams_season_two[season] = {}

            teams_season_two[season][team_two] = teams_season_two[season].get(
                team_two, 0)+1

        for key in teams_season_one:
            if key in teams_season_two:
                for i in teams_season_one[key]:
                    if i in teams_season_two[key]:
                        teams_season_one[key][i] = teams_season_one[key][i] + teams_season_two[key][i]

        teams_season = dict(sorted(teams_season_one.items()))

    return JsonResponse(teams_season, safe=False)

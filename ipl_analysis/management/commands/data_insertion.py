import csv
from django.core.management.base import BaseCommand
from ipl_analysis.models import Deliveries, Matches, Umpires


class Command(BaseCommand):
    help = 'Insert data into models'

    def handle(self, *args, **options):
        try:
            with open('data_source/deliveries.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)
                delivery_list = []
                for row in csv_reader:
                    delivery_obj = Deliveries(
                        delivery_id=int(row[0]),
                        inning=row[1],
                        batting_team=row[2],
                        bowling_team=row[3],
                        batsman=row[4],
                        bowler=row[5],
                        batsman_runs=int(row[6]),
                        total_runs=int(row[7])
                    )
                    delivery_list.append(delivery_obj)
                Deliveries.objects.bulk_create(delivery_list)
        except Exception as e:
            print(e)

        try:
            with open('data_source/matches.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)
                for row in csv_reader:
                    Matches.objects.create(
                        match_id=int(row[0]),
                        season=int(row[1]),
                        city=row[2],
                        date=row[3],
                        first_team=row[4],
                        second_team=row[5],
                        toss_winner=row[6],
                        toss_decision=row[7],
                        result=row[8],
                        dl_applied=int(row[9]),
                        winner=row[10],
                        win_by_runs=int(row[11]),
                        win_by_wickets=int(row[12]),
                        player_of_match=row[13],
                        venue=row[14],
                        umpire1=row[15],
                        umpire2=row[16],
                        umpire3=row[17]
                    )
        except Exception:
            print('error while loading matches data')

        try:
            with open('data_source/umpires.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                next(csv_reader)
                for row in csv_reader:
                    Umpires.objects.create(
                        umpire=row[0],
                        nationality=row[1],
                        first_officiated=int(row[2]),
                        last_officiated=int(row[3]),
                        no_of_matches=int(row[4])
                    )
        except Exception:
            print('error while loading umpires data')

        self.stdout.write(
            self.style.SUCCESS("Successfully loaded csv data into database")
        )

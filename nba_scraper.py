import pandas as pd
import argparse as ap
import urllib.request
import json


class TeamModel:

    def __init__(self, team, season, season_type):
        self.BASE_URL = 'http://stats.nba.com/stats/'
        self.TEAM_LOG_URL = self.BASE_URL + 'teamgamelog?'

        self.team = team
        self.season = season
        self.season_type = season_type
        self.json_url = self._build_url()
        self.page_data = self._get_page_data()

        DEBUG = 12

    def _get_page_data(self):
        with urllib.request.urlopen(self.json_url) as url:
            return json.loads(url.read().decode())

    def _build_url(self):
        parameter_list = ['TeamID=', 'Season=', 'SeasonType=']
        parameter_values = [self._get_team_id(), self.season, self.season_type]

        url = self.TEAM_LOG_URL
        for param, val in zip(parameter_list, parameter_values):
            url += param + val + '&'
        return url[:-1]

    def _get_team_id(self):
        team_dict = {'Celtics': '1610612738',
                     'Nets': '1610612751',
                     'Knicks': '1610612752',
                     'Sixers': '1610612755',
                     'Raptors': '1610612761',
                     'Bulls': '1610612741',
                     'Cavaliers': '1610612739',
                     'Pistons': '1610612765',
                     'Pacers': '1610612754',
                     'Bucks': '1610612749',
                     'Hawks': '1610612737',
                     'Hornets': '1610612766',
                     'Heat': '1610612748',
                     'Magic': '1610612753',
                     'Wizards': '1610612764',
                     'Nuggets': '1610612743',
                     'Timberwolves': '1610612750',
                     'Thunder': '1610612760',
                     'Trail Blazers': '1610612757',
                     'Jazz': '1610612762',
                     'Warriors': '1610612744',
                     'Clippers': '1610612746',
                     'Lakers': '1610612747',
                     'Suns': '1610612756',
                     'Kings': '1610612758',
                     'Mavericks': '1610612742',
                     'Rockets': '1610612745',
                     'Grizzlies': '1610612763',
                     'Pelicans': '1610612740',
                     'Spurs': '1610612759'}
        return team_dict[self.team]


def parse_command_line():
    parser = ap.ArgumentParser()
    parser.add_argument('team', nargs=1, help='name of team')
    parser.add_argument('season', nargs=1, help='years of season yyyy-yy')
    parser.add_argument('season_type', nargs=1, help='Regular Season or Playoffs or Pre Season')

    args = parser.parse_args()

    team = args.team[0]
    season = args.season[0]
    season_type_list = args.season_type[0].split('_')
    season_type = "" + season_type_list[0] + '%20' + season_type_list[1]

    actual_game_log_string = 'http://stats.nba.com//stats/teamgamelog?TeamID=1610612752&Season=2017-18&SeasonType=Regular%20Season'

    return team, season, season_type


def main():
    team, season, season_type = parse_command_line()
    a_season = TeamModel(team, season, season_type)



if __name__ == '__main__':
    main()

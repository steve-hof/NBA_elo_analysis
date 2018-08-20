import pandas as pd
import argparse as ap
import urllib.request
import json

from urllib.error import URLError, HTTPError, ContentTooShortError


class TeamModel:

    def __init__(self, team, season, season_type):
        self.BASE_URL = 'http://stats.nba.com/stats/'
        self.TEAM_LOG_URL = self.BASE_URL + 'teamgamelog?'
        self.header_data = {  # got the header from the py goldsberry library
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'en-US,en;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9' \
                      ',image/webp,*/*;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive'
        }
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'

        self.team = team
        self.season = season
        self.season_type = season_type
        self.json_url = self._build_url()
        # self.page_data = self._get_page_data()
        self.html_data = self._download()

    def fit(self):
        self._parse_data()

    def _parse_data(self):
        data = self.html_data
        headers = data['resultSets'][0]['headers']
        games_list = []
        bla = data['resultSets'][0]['rowSet']
        for game in data['resultSets'][0]['rowSet']:
            games_list.append(game)

        df = pd.DataFrame(games_list, columns=headers)

        DEBUG = 8

    def _download(self, num_retries=2):
        print('Downloading:', self.json_url)
        request = urllib.request.Request(self.json_url)
        request.add_header('User-agent', self.user_agent)
        try:
            # with urllib.request.urlopen(json_url) as url:
            #     data = json.loads(url.read().decode())
            # html = urllib.request.urlopen(request).read().decode()
            with urllib.request.urlopen(request) as url:
                html = json.loads(url.read().decode())
        except (URLError, HTTPError, ContentTooShortError) as e:
            print('Download error:', e.reason)
            html = None
            if num_retries > 0:
                if hasattr(e, 'code') and 500 <= e.code < 600:
                    # recursively retry 5xx HTTP errors
                    return self._download(self.json_url, num_retries - 1)
        return html

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
    knicks_17_18 = TeamModel(team, season, season_type)
    knicks_17_18.fit()

    DEBUG = 1024

if __name__ == '__main__':
    main()

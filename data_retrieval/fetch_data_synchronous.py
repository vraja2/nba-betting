import json
import os
import requests

USER_AGENT = "curl"
REFERER = "http://stats.nba.com/"
HEADERS = {'user-agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/45.0.2454.101 Safari/537.36'),
           'referer': 'http://stats.nba.com/scores/'}
NUM_GAMES_PER_SEASON = 30*82/2

endpoint = 'http://stats.nba.com/stats/{}?GameID={}&StartPeriod=0&EndPeriod=0&StartRange=0&EndRange=0&RangeType=0'

def make_request_to_nba_stats(url):
  return requests.get(url, headers=HEADERS).json()

def get_boxscore_data_for_game(game_id):
  url_paths = ['boxscoretraditionalv2', 'boxscoreadvancedv2', 'boxscoremiscv2', 'boxscorescoringv2', 'boxscoreusagev2',
               'boxscorefourfactorsv2', 'boxscoreplayertrackv2', 'hustlestatsboxscore', 'boxscoresummaryv2']

  boxscore_data = {}

  # TODO: parallelize these url requests
  for path in url_paths:
    boxscore_data[path] = make_request_to_nba_stats(endpoint.format(path, game_id))

  return boxscore_data

def get_boxscore_data_for_game_wrapper(game_id):
  print "Game ID {}".format(game_id)
  with open(os.path.join('data', '{}.json'.format(game_id)), 'w') as outfile:
    json.dump(get_boxscore_data_for_game(game_id), outfile)

def get_boxscore_data_for_season(season):
  for game_num in range(1, NUM_GAMES_PER_SEASON+1):
    get_boxscore_data_for_game_wrapper('002{:02}0{:04}'.format(season, game_num))

def main():
  if not os.path.exists('data'):
    os.makedirs('data')
  seasons = range(16, 18)
  for season in seasons:
    get_boxscore_data_for_season(season)

if __name__ == '__main__':
  main()
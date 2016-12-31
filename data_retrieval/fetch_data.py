import json
import os
import requests
from threading import Thread
from Queue import Queue

NUM_THREADS = 8

USER_AGENT = "curl"
REFERER = "http://stats.nba.com/"
HEADERS = {'User-Agent': USER_AGENT, 'referer': REFERER}
NUM_GAMES_PER_SEASON = 30*82/2

endpoint = 'http://stats.nba.com/stats/{}/?GameID={}&StartPeriod=0&EndPeriod=0&StartRange=0&EndRange=0&RangeType=0'

task_queue = Queue()

def make_request_to_nba_stats(url):
  return requests.get(url, headers=HEADERS).json()

def get_boxscore_data_for_game_thread():
  while True:
    game_id = task_queue.get()
    print "Game ID {}".format(game_id)
    with open(os.path.join('data', '{}.json'.format(game_id)), 'w') as outfile:
      json.dump(get_boxscore_data_for_game(game_id), outfile)
      task_queue.task_done()

def get_boxscore_data_for_game(game_id):
  url_paths = ['boxscoretraditionalv2', 'boxscoreadvancedv2', 'boxscoremiscv2', 'boxscorescoringv2', 'boxscoreusagev2',
               'boxscorefourfactorsv2', 'boxscoreplayertrackv2', 'hustlestatsboxscore', 'boxscoresummaryv2']

  boxscore_data = {}

  # TODO: parallelize these url requests
  for path in url_paths:
    boxscore_data[path] = make_request_to_nba_stats(endpoint.format(path, game_id))

  return boxscore_data

def get_boxscore_data_for_season(season):
  for game_num in range(1, NUM_GAMES_PER_SEASON+1):
    task_queue.put('002{:02}0{:04}'.format(season, game_num))
  task_queue.join()

def init_worker_threads():
  for i in range(NUM_THREADS):
    t = Thread(target=get_boxscore_data_for_game_thread)
    t.daemon = True
    t.start()

def main():
  if not os.path.exists('data'):
    os.makedirs('data')
  init_worker_threads()
  seasons = range(0, 17)
  for season in seasons:
    get_boxscore_data_for_season(season)

if __name__ == '__main__':
  main()
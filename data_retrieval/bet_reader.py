import BeautifulSoup
import datetime
import numpy
import pickle
import requests

SEASON_1617_START = datetime.datetime.strptime('2016-10-25', '%Y-%m-%d')
SEASON_1617_END = datetime.datetime.strptime('2017-04-13', '%Y-%m-%d')
SEASON_1516_START = datetime.datetime.strptime('2015-10-27', '%Y-%m-%d')
SEASON_1516_END = datetime.datetime.strptime('2016-04-16', '%Y-%m-%d')
SEASON_1415_START = datetime.datetime.strptime('2014-10-28', '%Y-%m-%d')
SEASON_1415_END = datetime.datetime.strptime('2015-04-15', '%Y-%m-%d')
SEASON_1314_END = datetime.datetime.strptime('2014-04-16', '%Y-%m-%d')

def fix_game(game):
  fixes = {
    'Milwaukee': 'Bucks',
    'Trail': 'Trail Blazers',
    'Trailblazers': 'Trail Blazers',
    'Trail Blaze': 'Trail Blazers',
  }
  for key in ('home', 'away'):
    if key in game and game[key] in fixes:
      game[key] = fixes[game[key]]

def transform_old_format(old_bet_info):
  bet_info = []
  for day_str, games in old_bet_info.iteritems():
    for game in games:
      fix_game(game)
      bet_info.append({
        'home': game['home'],
        'away': game['away'],
        'overunder': game['overunder'],
        'date': datetime.datetime.strptime(day_str, '%Y-%m-%d') - datetime.timedelta(days=1),
        })
  return bet_info

def read_info(filename="bet_info_2016_2017_last_day.pkl", start_date=SEASON_1617_START_TMP, end_date=SEASON_1617_END_TMP):
  try:
    with open(filename, 'rb') as f:
      bet_info_s15 = pickle.load(f)
  except:
    print 'Downloading betting info from {} to {}.\nThis should only need to be done once...'.format(
      start_date,
      end_date,
    )

    request_headers = {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/60.0.3112.101 Safari/537.36'
    }

    bet_info = {}
    day = end_date
    while day >= start_date:
      print day
      if day.month == 7:
        print "Skipping Summer"
        day = day - datetime.timedelta(days=90)
        continue
      page_url = 'http://data.nowgoal.com/nba/oddsHistory.aspx?Selday={day}'.format(day=day)
      print page_url
      page = None
      for _ in range(5):
        try:
          page = requests.get(page_url, timeout=10, headers=request_headers)
        except:
          print "retrying..."
          continue
      if page == None:
        print "Failed to get bets for {} after 5 retries.".format(day)
        continue

      soup = BeautifulSoup.BeautifulSoup(page.text)
      rows = soup.findAll(id='Sclass_1') # Sclass_1 = NBA
      if len(rows) > 0:
        bet_info[day] = []
      for row in rows:
        try:
          if len(row) < 11:
            continue
          overunder = float(row.findAll("td")[10].find("a").contents[0]) # Bet365
          line = float(row.findAll("td")[5].find("a").contents[0]) # Bet365
          trows = row.find(align='left').findAll(target="_blank") # Team names
          assert len(trows) == 2
          home = trows[0].contents[0].strip()
          away = trows[1].contents[0].strip()
          bet_info[day].append({
              "home": home,
              "away": away,
              "overunder": overunder,
              "line": line
            })
        except IndexError:
          continue
      day = day - datetime.timedelta(days=1)

    bet_info_s15 = {}
    for day, info in bet_info.iteritems():
      if day >= start_date and day <= end_date:
        bet_info_s15[day.strftime('%Y-%m-%d')] = info

    with open(filename, "wb") as f:
      pickle.dump(bet_info_s15, f)
  return bet_info_s15

if __name__ == "__main__":
  bet_info = read_info()
  bet_info = transform_old_format(bet_info)
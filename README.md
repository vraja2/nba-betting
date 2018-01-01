# NBA Betting

## Evaluation Methodology

### Spread Simulation

Compute predicted score delta (from the perspective of the away team) and bet on a direction with respect to the line
from scraped historical spread data. If the direction matches the actual score delta, the bet is deemed a winner and
otherwise, a loser.

### Methods

#### Linear Regression (Baseline)

##### Features:

away stats (19), home stats (19) = 38 total features

*FGM, FGA, FG%, 3PM, 3PA, 3P%, FTM, FTA, FT%, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS, PLUSMINUS*

##### Results:
0 games in  
Win Percent: 0.515650741351  
Loss Percent: 0.484349258649  
Bets placed: 1214  
Bets not placed: 0  

400 games in  
Win Percent: 0.527027027027  
Loss Percent: 0.472972972973  
Bets placed: 814  
Bets not placed: 0  

800 games in  
Win Percent: 0.548309178744  
Loss Percent: 0.451690821256  
Bets placed: 414  
Bets not placed: 0

1000 games in  
Win Percent: 0.584112149533  
Loss Percent: 0.415887850467  
Bets placed: 214  
Bets not placed: 0

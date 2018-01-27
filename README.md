# NBA Betting

## Evaluation Methodology

### Training and testing sets

Train on 2000-2016 data, evaluate on 2016-2017 season. In the future, would like to do K-fold
cross-validation omitting 1 season at a time.

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
**0 games in**  
Win Percent: 0.515650741351  
Loss Percent: 0.484349258649  
Bets placed: 1214  
Bets not placed: 0  

**400 games in**  
Win Percent: 0.527027027027  
Loss Percent: 0.472972972973  
Bets placed: 814  
Bets not placed: 0  

**800 games in**  
Win Percent: 0.548309178744  
Loss Percent: 0.451690821256  
Bets placed: 414  
Bets not placed: 0

**1000 games in**  
Win Percent: 0.584112149533  
Loss Percent: 0.415887850467  
Bets placed: 214  
Bets not placed: 0

#### Artificial Neural Network

##### Features:

away stats (19), home stats (19) = 38 total features

*FGM, FGA, FG%, 3PM, 3PA, 3P%, FTM, FTA, FT%, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS, PLUSMINUS*

##### Results:
**0 games in**  
Win Percent: 0.511532125206  
Loss Percent: 0.488467874794  
Bets placed: 1214  
Bets not placed: 0

**400 games in**  
Win Percent: 0.530712530713  
Loss Percent: 0.469287469287  
Bets placed: 814  
Bets not placed: 0

**800 games in**  
Win Percent: 0.553140096618  
Loss Percent: 0.446859903382  
Bets placed: 414  
Bets not placed: 0

**1000 games in**  
Win Percent: 0.579439252336  
Loss Percent: 0.420560747664  
Bets placed: 214  
Bets not placed: 0

#### Lasso Regression

alpha = 0.1

##### Features:

away stats (19), home stats (19) = 38 total features

*FGM, FGA, FG%, 3PM, 3PA, 3P%, FTM, FTA, FT%, OREB, DREB, REB, AST, STL, BLK, TOV, PF, PTS, PLUSMINUS*

##### Results:
**0 games in**  
Win Percent: 0.518945634267  
Loss Percent: 0.481054365733   
Bets placed: 1214   
Bets not placed: 0

**400 games in**  
Win Percent: 0.534398034398  
Loss Percent: 0.465601965602  
Bets placed: 814  
Bets not placed: 0  

**800 games in**  
Win Percent: 0.562801932367  
Loss Percent: 0.437198067633  
Bets placed: 414  
Bets not placed: 0  

**1000 games in**  
Win Percent: 0.593457943925  
Loss Percent: 0.406542056075  
Bets placed: 214  
Bets not placed: 0

# Heuristic Bot for Schnapsen
## Overview
This bot is designed for playing Schnapsen with heuristic-based decision-making to enhance its gameplay strategy. It evaluates moves by prioritizing marriages, low-value cards early, and strategic trick-winning.It is an enhanced version of random bot 
## Features
- Prioritizes marriages for bonus points.
- Saves high-value cards for critical moments.
- Adapts strategies based on early and late-game situations.
## How to Use
1. Ensure the `schnapsen` library is installed.
2. Import `HeuristicBot` into your Schnapsen game setup.
3. Instantiate the bot with a random generator:
   ```python
   from random import Random
   bot = HeuristicBot(rand=Random(), name="HeuristicBot")
-------------------------------------------------------------------------------------------------------------------------------------
# Schnapsen Bot Tournament(heuristic bot vs rdeep bot)
This Python script facilitates tournament play between different Schnapsen card game bots, specifically comparing a HeuristicBot against RdeepBot. The script allows for multiple games to be played and tracks statistics about bot performance.
## Prerequisites
The following Python packages are required:
- `schnapsen.game`
- `schnapsen.bots`
- `random`
Your custom `heuristic_bot.py` file containing the `HeuristicBot` class implementation must be in the same directory.
## Features
- Single game matches between two bots
- Multiple game tournaments
- Detailed game results including points and scores
- Tournament statistics and win rates
- Support for different bot types (HeuristicBot and RdeepBot)
## Code Structure
The code consists of several main components:
### Bot Initialization
```python
heuristic_bot = HeuristicBot(rand=random.Random(), name="HeuristicBot")
rdeepbot = RdeepBot(num_samples=10, depth=5, rand=random.Random())
```
### Main Functions
1. `play_game(bot1, bot2)`:
   - Plays a single game between two bots
   - Returns the winner (0 for bot1, 1 for bot2)
   - Prints detailed game results

2. `play_multiple_games(bot1, bot2, num_games)`:
   - Runs multiple games between two bots
   - Tracks win counts for both bots
   - Returns a tuple of win counts

3. `get_bot_name(bot)`:
   - Helper function to get the display name of a bot
   - Supports HeuristicBot and RdeepBot types
## Usage
1. Configure the number of games:
```python
num_games = 1000  # Set the desired number of games
```
2. Set up the opponent bots:
```python
bots = [rdeepbot]  # Add more bots to this list if needed
```
3. Run the script:
```bash
python schnapsen_tournament.py
```
## Output
The script provides detailed output including:
- Individual game results
- Points and scores for each game
- Match summaries
- Final tournament results with win rates
Example output:
```
Final Tournament Results:
======================================================================
HeuristicBot vs RdeepBot:
Score: 187 - 813
HeuristicBot Win Rate: 18.70%
```
## Customization
To add more bots to the tournament:
1. Import the bot class
2. Initialize the bot with desired parameters
3. Add the bot instance to the `bots` list

## Notes
- The script uses a fixed random seed (42) for game play to ensure reproducibility
- Games are played sequentially and results are stored in a dictionary
- Win rates are calculated and displayed as percentages
## Contributing
To extend this tournament system:
1. Create new bot classes that implement the required game interface
2. Add support for new bot types in the `get_bot_name()` function
3. Add new bot instances to the `bots` list
-------------------------------------------------------------------------------------------------------------------------------------
# Schnapsen Random Bot Tournament(Randomot vs rdeep bot)
This Python script implements a tournament system for the Schnapsen card game, specifically comparing a Random bot (RandBot) against other bot implementations like RdeepBot. The system allows for multiple games and tracks comprehensive statistics about bot performance.
## Prerequisites
Required Python packages:
- `schnapsen.game`
- `schnapsen.bots`
- `random`
## Features
- Single game matches between RandBot and other bots
- Support for multi-game tournaments
- Detailed game-by-game results
- Comprehensive tournament statistics
- Win rate calculations
- Support for different bot types (currently RandBot and RdeepBot)
## Code Structure
### Bot Initialization
```python
random_bot = RandBot(random.Random())
rdeepbot = RdeepBot(num_samples=10, depth=5, rand=random.Random())
```
### Core Functions
1. `play_game(bot1, bot2)`:
   - Executes a single game between two bots
   - Outputs detailed game results
   - Returns: 0 if bot1 wins, 1 if bot2 wins
   - Includes points and score information

2. `play_multiple_games(bot1, bot2, num_games)`:
   - Manages multiple games between two bots
   - Keeps track of wins for each bot
   - Returns: Tuple containing win counts for both bots

3. `get_bot_name(bot)`:
   - Utility function for bot name identification
   - Supports RandBot and RdeepBot types
   - Returns readable names for display purposes
## Usage
1. Set the number of games to play:
```python
num_games = 1000  # Adjust as needed
```
2. Configure opponent bots:
```python
bots = [rdeepbot]  # Add more bots to this list if desired
```
3. Run the tournament:
```bash
python random_bot_tournament.py
```
## Output Format
The script provides several levels of output:
### Game Details
```
Game Details:
Winner: RdeepBot
Points: 66
Score: (2, 1)
--------------------------------------------------
Match Summary:
RandomBot vs RdeepBot: 55 - 945

Final Tournament Results:
======================================================================
RandomBot vs RdeepBot:
Score: 55 - 945
RandomBot Win Rate: 5.50%
## Customization
To extend the tournament:
1. Import additional bot classes from `schnapsen.bots`
2. Initialize new bot instances with desired parameters
3. Add new bots to the `bots` list
4. Update the `get_bot_name()` function to support new bot types
## Implementation Notes
- Uses a fixed random seed (42) for reproducibility
- Results are stored in a dictionary for easy access
- Win rates are calculated and displayed as percentages
- Games are played sequentially with detailed logging
## Differences from Other Implementations
This version specifically focuses on RandBot as the primary player, which:
- Uses completely random move selection
- Serves as a baseline for comparing more sophisticated bots
- Helps establish a performance floor for bot evaluation
-------------------------------------------------------------------------------------------------------------------------------------
# Bot Performance Statistical Analysis
## Overview
This Python script performs a statistical analysis to compare the performance of HeuristicBot and RandomBot when playing against RDeepBot. It uses a proportions z-test to determine if there is a statistically significant difference in the win rates of the two bots.
## Prerequisites
### Required Libraries
- `statsmodels`
- `numpy` (typically installed with statsmodels)
### Installation
```bash
pip install statsmodels
```
## Script Functionality
The script does the following:
1. Loads experimental data on bot wins
2. Performs a proportions z-test
3. Calculates and displays win rates
4. Provides statistical significance interpretation

## Usage
```python
from statsmodels.stats.proportion import proportions_ztest
import random  # For potential future randomization needs

# Input your experimental data
k1 = 194  # Wins by HeuristicBot
N1 = 1000  # Total games HeuristicBot played
k2 = 65   # Wins by RandomBot
N2 = 1000  # Total games RandomBot played

# Run the analysis
zscore, pval = proportions_ztest([k1, k2], [N1, N2])
```

## Output Explanation

The script provides:
- Win rates for both bots
- Z-Score: Measures the statistical difference between proportions
- P-Value: Indicates statistical significance

### Interpretation of P-Value
- P-value < 0.05: Statistically significant difference
- P-value ≥ 0.05: No statistically significant difference

## Example Output
```
HeuristicBot vs. RDeepBot Wins: 194/1000 (19.40%)
RandomBot vs. RDeepBot Wins: 65/1000 (6.50%)
Z-Score: 8.123
P-Value: 0.0000004
There is a significant difference in win rates between HeuristicBot and RandomBot when playing against RDeepBot.
```

## Statistical Method

### Proportions Z-Test
- Compares win rates of two groups
- Determines if the difference in proportions is statistically significant
- Null Hypothesis: No difference in win rates
- Alternative Hypothesis: Significant difference in win rates

## Limitations
- Assumes large sample size
- Requires independent samples
- Only tests for statistical significance, not effect size

## Potential Improvements
- Add confidence interval calculation
- Implement effect size measurement
- Create visualization of results

## References
- statsmodels documentation
- Statistical hypothesis testing principles
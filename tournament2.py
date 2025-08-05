from schnapsen.game import SchnapsenGamePlayEngine
from schnapsen.bots import RdeepBot, RandBot
import random
random_bot = RandBot(random.Random())  # Initializing random bot
rdeepbot = RdeepBot(num_samples=10, depth=5, rand=random.Random())  # Initialize RdeepBot
bots = [rdeepbot]  # opponents
num_games = 1000  # number of games
# Function to play a single game
def play_game(bot1, bot2):
    """
    Play a single game between two bots and print the detailed result
    Args:
        bot1: The first bot (Player 1)
        bot2: The second bot (Player 2)
    Returns:
        int: 0 if bot1 won, 1 if bot2 won
    """
    engine = SchnapsenGamePlayEngine()
    # Get the game result - returns (winner_bot, points, score)
    winner_bot, points, score = engine.play_game(bot1, bot2, random.Random(42))
    # Print detailed game result
    print(f"\nGame Details:")
    print(f"Winner: {get_bot_name(winner_bot)}")
    print(f"Points: {points}")
    print(f"Score: {score}")
    print("-" * 50)
    # Return 0 if bot1 won, 1 if bot2 won
    return 0 if winner_bot is bot1 else 1
# Function to play multiple games
def play_multiple_games(bot1, bot2, num_games):
    """
    Play multiple games between two bots and track their win counts
    Args:
        bot1: The first bot (Player 1)
        bot2: The second bot (Player 2)
        num_games: The number of games to play
    Returns:
        tuple: (Number of wins by bot1, Number of wins by bot2)
    """
    bot1_wins = 0
    bot2_wins = 0
    for game_num in range(num_games):
        print(f"\nPlaying Game {game_num + 1}")
        winner = play_game(bot1, bot2)
        if winner == 0:
            bot1_wins += 1
        else:
            bot2_wins += 1
    return bot1_wins, bot2_wins
# Helper function to get bot name
def get_bot_name(bot):
    """
    Get the name of the bot for display purposes
    Args:
        bot: The bot instance
    Returns:
        str: The name of the bot
    """
    if isinstance(bot, RandBot):
        return "RandomBot"
    elif isinstance(bot, RdeepBot):
        return "RdeepBot"
    return str(bot)
# Play the tournament
results = {}
for bot in bots:
    print(f"\nStarting matches between {get_bot_name(random_bot)} and {get_bot_name(bot)}")
    print("=" * 70)
    bot1_wins, bot2_wins = play_multiple_games(random_bot, bot, num_games)
    results[(get_bot_name(random_bot), get_bot_name(bot))] = (bot1_wins, bot2_wins)
    print(f"\nMatch Summary:")
    print(f"{get_bot_name(random_bot)} vs {get_bot_name(bot)}: {bot1_wins} - {bot2_wins}")

# Print the final results
print("\nFinal Tournament Results:")
print("=" * 70)
for (bot1_name, bot2_name), (bot1_wins, bot2_wins) in results.items():
    win_percentage = (bot1_wins / (bot1_wins + bot2_wins)) * 100
    print(f"{bot1_name} vs {bot2_name}:")
    print(f"Score: {bot1_wins} - {bot2_wins}")
    print(f"{bot1_name} Win Rate: {win_percentage:.2f}%")
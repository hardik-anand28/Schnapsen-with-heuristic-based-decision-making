from schnapsen.game import SchnapsenGamePlayEngine
from schnapsen.bots import RdeepBot
from heuristic_bot import HeuristicBot
import random
#initialize your heuristic bot
heuristic_bot = HeuristicBot(rand=random.Random(), name="HeuristicBot")
#initialize RdeepBot with parameters
rdeepbot = RdeepBot(num_samples=10, depth=5, rand=random.Random())
#store RdeepBot in a list for tournament play
bots = [rdeepbot]#opponent bots
num_games = 1000#number of games to play
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
    winner_bot, points, score = engine.play_game(bot1, bot2, random.Random(42))
    #print detailed game result
    print(f"\nGame Details:")
    print(f"Winner: {get_bot_name(winner_bot)}")
    print(f"Points: {points}")
    print(f"Score: {score}")
    print("-" * 50)
    #return the winner identifier
    return 0 if winner_bot is bot1 else 1
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
def get_bot_name(bot):
    """
    Get the name of the bot for display purposes
    Args:
        bot: The bot instance
    Returns:
        str: The name of the bot
    """
    if isinstance(bot, HeuristicBot):
        return "HeuristicBot"
    elif isinstance(bot, RdeepBot):
        return "RdeepBot"
    return str(bot)
#play the tournament and store results
results = {}
for bot in bots:
    print(f"\nStarting matches between {get_bot_name(heuristic_bot)} and {get_bot_name(bot)}")
    print("=" * 70)
    bot1_wins, bot2_wins = play_multiple_games(heuristic_bot, bot, num_games)
    results[(get_bot_name(heuristic_bot), get_bot_name(bot))] = (bot1_wins, bot2_wins)
    print(f"\nMatch Summary:")
    print(f"{get_bot_name(heuristic_bot)} vs {get_bot_name(bot)}: {bot1_wins} - {bot2_wins}")
#print the final results
print("\nFinal Tournament Results:")
print("=" * 70)
for (bot1_name, bot2_name), (bot1_wins, bot2_wins) in results.items():
    win_percentage = (bot1_wins / (bot1_wins + bot2_wins)) * 100
    print(f"{bot1_name} vs {bot2_name}:")
    print(f"Score: {bot1_wins} - {bot2_wins}")
    print(f"{bot1_name} Win Rate: {win_percentage:.2f}%")

import random
from typing import Optional, List
from schnapsen.game import Bot, PlayerPerspective, Move
from schnapsen.deck import Card, Rank, Suit

class HeuristicBot(Bot):
    """
    An enhanced bot that uses heuristics to make better decisions during gameplay
    The bot balances strategic play with randomness and uses rules to prioritize actions
    and have different strategies for early and late phase of game.
    """
    def __init__(self, rand: random.Random, name: Optional[str] = None) -> None:
        """
        Initialize the bot with a random generator and an optional name.
        Args:
            rand: A random number generator for decision-making.
            name: An optional name for the bot.
        """
        super().__init__(name)
        self.rng = rand
    def get_move(self, perspective: PlayerPerspective, leader_move: Optional[Move]) -> Move:
        """
        Determine the bot's next move based on the current game state.
        Args:
            perspective: The bot's view of the game, including hand and valid moves.
            leader_move: The move made by the leader, or None if this bot is the leader.
        Returns:
            The selected move for the current turn.
        """
        moves: List[Move] = perspective.valid_moves()
        # phase one: Check for marriages
        marriage_move = self.find_marriage_move(moves)
        if marriage_move:
            return marriage_move
        # leader or follower logic
        if leader_move is None:
            return self.get_leader_move(perspective, moves)# if this bot is the leader
        else:
            return self.get_follower_move(perspective, moves, leader_move)# if this bot is a follower
    
    def find_marriage_move(self, moves: List[Move]) -> Optional[Move]:
        """
        Marriages score points and should be prioritized
        This function checks for possible marriage moves and return one if available
        Args:
            moves: The list of valid moves for this turn
        Returns:
            A move that forms a marriage, or None if no such move exists
        """
        for move in moves:
            if move.is_marriage():
                return move
        return None
    
    def get_card_value(self, card: Card) -> int:
        """
        Get the point value of a card based on its rank
        Args:
            card: The card to evaluate
        Returns:
            The point value of the card
        """
        values = {
            Rank.ACE: 11,
            Rank.TEN: 10,
            Rank.KING: 4,
            Rank.QUEEN: 3,
            Rank.JACK: 2
        }
        return values.get(card.rank, 0)
    
    def is_high_value_card(self, card: Card) -> bool:
        """
        Check if card is high value (10 or Ace)
        Args:
            card: The card to evaluate
        Returns:
            True if the card is high value, False otherwise

        """
        return card.rank in [Rank.ACE, Rank.TEN]
    
    def get_leader_move(self, perspective: PlayerPerspective, moves: List[Move]) -> Move:
        """
        Determine the move to make when this bot is the leader
        Prioritize playing low-value non-trump cards early in the game
        Args:
            perspective: The bot's view of the game
            moves: The list of valid moves for this turn
        Returns:
            The selected move
        """
        # early game:prioritize low-value non-trump cards
        if len(perspective.get_hand()) > 3:# early game: more than 3 cards left.
            non_trump_moves = [
                move for move in moves 
                if not move.is_marriage() and 
                move.cards[0].suit != perspective.get_trump_suit() and
                not self.is_high_value_card(move.cards[0])
            ]
            if non_trump_moves:
                return min(non_trump_moves, key=lambda m: self.get_card_value(m.cards[0]))
        # late game: can use high-value cards
        return self.rng.choice(moves)# fallback to random if no good moves found
    
    def get_follower_move(self, perspective: PlayerPerspective, moves: List[Move], leader_move: Move) -> Move:
        """
        Handle moves when we are the follower
        Args:
            perspective: The bot's view of the game
            moves: The list of valid moves for this turn
            leader_move: The move made by the leader
        Returns:
            The selected move
        """
        # get the leading card and its value
        leading_card = leader_move.cards[0]
        leading_value = self.get_card_value(leading_card)
        
        # if we can't win the trick, play lowest value card
        winning_moves = []
        for move in moves:
            if not move.is_marriage():#don't consider marriages when following
                card = move.cards[0]
                #check if our card can win (same suit and higher value, or trump)
                if (card.suit == leading_card.suit and self.get_card_value(card) > leading_value) or \
                   (card.suit == perspective.get_trump_suit() and leading_card.suit != perspective.get_trump_suit()):
                    winning_moves.append(move)
        
        if not winning_moves:
            # can't win, play lowest value card
            return min(moves, key=lambda m: self.get_card_value(m.cards[0]))
        
        # if the trick is valuable (contains 10 or Ace)
        if self.is_high_value_card(leading_card):
            return self.rng.choice(winning_moves)  # Try to win valuable tricks
            
        # otherwise, try to save high-value cards
        non_high_value_winners = [
            move for move in winning_moves 
            if not self.is_high_value_card(move.cards[0])
        ]
        if non_high_value_winners:
            return self.rng.choice(non_high_value_winners)
            
        return self.rng.choice(moves)#fallback to random if no good moves found
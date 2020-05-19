#-----------------------------------------------------------------------
# Ambrose Ryan Xavier
#-----------------------------------------------------------------------

class Card:
    """Card Class for Representing and Manipulating One Playing Card"""

    def __init__(self, rank, suit):
        """A constructor method that sets the suit and rank"""
        self.suit = suit
        self.rank = rank
        self.value = self.assign_value(rank)

    def get_suit(self):
        """A reader method that returns the suit of the card"""
        return self.suit

    def get_rank(self):
        """A reader method that returns the rank of the card"""
        return self.rank

    def get_value(self):
        """A reader method that returns the blackjack value of the card"""
        return self.value

    def assign_value(self, rank):
        """A helper function to determine the blackjack value of a rank"""
        if self.rank == "ace":
            return 11
        elif self.rank == "two":
            return 2
        elif self.rank == "three":
            return 3
        elif self.rank == "four":
            return 4
        elif self.rank == "five":
            return 5
        elif self.rank == "six":
            return 6
        elif self.rank == "seven":
            return 7
        elif self.rank == "eight":
            return 8
        elif self.rank == "nine":
            return 9
        else:
            return 10
        # The default is ten, jack, queen, or king


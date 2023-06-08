class Card(object):
    """
        Represents the card
    """
    card_ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10',\
        'Jack', 'Queen', 'King', 'Ace')
    card_suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades')

    def __init__(self, rank: int=2, suit: str=0) -> None:
        """
            Initialize our rank and suit for the card
        """
        if isinstance(rank, str):
            rank = int(rank)
        if isinstance(suit, str):
            suit = int(suit)

        assert 14 >= rank >=2 and 3 >= suit >=0

        self.rank = rank
        self.suit = suit


    def __str__(self) -> str:
        """
            Represents the card as a str
        """
        return f"{Card.card_ranks[self.rank-2]} of {Card.card_suits[self.suit]}."


    def __gt__(self, other):
        if self.suit > other.suit:
            return True
        if self.suit < other.suit:
            return False
        if self.rank > other.rank:
            return True
        return False


    def __ge__(self, other):
        if self.suit >= other.suit:
            return True
        if self.suit < other.suit:
            return False
        if self.rank >= other.rank:
            return True
        return False


    def __lt__(self, other):
        if self.suit < other.suit:
            return True
        if self.suit > other.suit:
            return False
        if self.rank < other.rank:
            return True
        return False


    def __le__(self, other):
        if self.suit <= other.suit:
            return True
        if self.suit > other.suit:
            return False
        if self.rank <= other.rank:
            return True
        return False


    def __eq__(self, other):
        if self.suit == other.suit and self.rank == other.rank:
            return True
        return False


    def  __ne__(self, other):
        if self.suit != other.suit and self.rank != other.rank:
            return True
        return False


class Deck(object):
    """
        Represents the deck
    """
    def __init__(self) -> None:
        """
            Initialize our deck and adds to self.cards all the unique cards
        """
        self.cards = []

        for suit in range(0, 4):
            for rank in range(2, 15):
                card = Card(rank=rank, suit=suit)
                self.cards.append(card)


    def __str__(self) -> str:
        """
            Represents the deck as one string
        """
        res = []

        for card in self.cards:
            res.append(str(card))

        return "\n".join(res)


def main() -> None:
    """
        The main function for this script.
    """
    card_1 = Card()
    card_2 = Card(14, 2)

    print(f"The first card is the {card_1}")
    print(f"The second card is the {card_2}")

    deck = Deck()
    print(deck)
    #print(deck.cards)


if __name__ == "__main__":
    main()

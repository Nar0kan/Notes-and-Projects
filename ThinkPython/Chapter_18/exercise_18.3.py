from practice_cards import Card
from random import randint, shuffle


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


    def pop_card(self) -> Card:
        """
            Removes a last card from the deck and returns it
        """
        return self.cards.pop()


    def add_card(self, card: Card) -> None:
        """
            Adds a new card to the deck
        """
        self.cards.append(card)


    def shuffle(self):
        """
            Shuffles the deck
        """
        shuffle(self.cards)


    def sort(self, order: str="ascending"):
        """
            Sorts the cards in the deck
        """
        try:
            return quick_sort(self.cards, order)
        except TypeError:
            print("Order must be either 'ascending' or 'descending'")


    def move_cards(self, hand, num) -> None:
        """
            Moves a card from the 'deck' to the 'hand' 'num' times
        """
        for n in range(num):
            hand.add_card(self.pop_card())


    def deal_hands(self, hands: int, cards: int) -> list:
        hands_list = []

        for hand in range(hands):
            player_hand = Hand("Player " + str(hand))
            self.move_cards(player_hand, cards)
            hands_list.append(player_hand)

        return hands_list


class Hand(Deck):
    """
        Represents a hand of playing cards.
    """
    def __init__(self, label='') -> None:
        """
            Initialize new hand
        """
        self.cards = []
        self.label = label


def quick_sort(L, order="ascending"):
    """
        Quicksort function
    """
    if len(L) <= 1:
        return L
    smaller, equal, larger = [], [], []
    pivot = L[randint(0, len(L) - 1)]

    for x in L:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)

    larger = quick_sort(larger, order=order)
    smaller = quick_sort(smaller, order=order)

    if order=="ascending":
        final = smaller + equal + larger
    else:
        final = larger + equal + smaller
    return final


def find_defining_class(obj, meth_name) -> type:
    for t in type(obj).mro():
        if meth_name in t.__dict__:
            return t


def main() -> None:
    """
        The main function for this script.
    """
    card_1 = Card()
    card_2 = Card(14, 2)

    print(f"The first card is the {card_1}")
    print(f"The second card is the {card_2}")

    deck = Deck()
    #print(deck)

    deck.shuffle()

    players_hands = deck.deal_hands(4, 2)

    for hand in players_hands:
        print(hand.label,"\n", hand, '\n')
    
    print(find_defining_class(hand, 'shuffle'))


if __name__ == "__main__":
    main()

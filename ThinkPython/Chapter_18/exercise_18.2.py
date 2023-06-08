from practice_cards import Card
from random import shuffle, randint


class Deck(object):
    """
        Represents the deck
    """
    def __init__(self) -> None:
        """
            Initialize our deck and adds to self.cards all the unique cards
        """
        self.cards = []

        for suit in range(2, 4):
            for rank in range(2, 15):
                card = Card(rank=rank, suit=suit)
                self.cards.append(card)

        for suit in range(0, 2):
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


def main() -> None:
    """
        The main function for this script.
    """
    card_1 = Card()
    card_2 = Card(14, 2)

    print(f"The first card is the {card_1}")
    print(f"The second card is the {card_2}")

    deck = Deck()
    print("Unsorted deck:\n", deck, "\n\n")

    deck.cards =  deck.sort()
    print("Sorted deck:\n", deck, "\n\n")

    deck.cards = deck.sort(order='descending')
    print("Sorted deck:\n", deck, "\n\n")


if __name__ == "__main__":
    main()

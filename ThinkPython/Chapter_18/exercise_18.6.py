from Card import Card, Hand, Deck
from collections import Counter
from pprint import pprint


class PokerHand(Hand):
    """Represents a poker hand."""

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.
        Stores the result in attribute suits.
        """
        self.suits = {}

        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1


    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.
        Stores the result in attribute ranks.
        """
        self.ranks = {}

        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1


    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
        Works with len(self.cards), so it's not only higher than 5 now.
        """
        for val in self.suits.values():
            if val >= int(len(self.cards)-2):
                return True

        return False


    def has_pair(self, pair_count: int=2):
        """
            Returns True if the hand has a pair, False otherwice.
        """
        for val in self.ranks.values():
            if val >= pair_count:
                return True

        return False


    def has_two_pair(self):
        """
            Returns True if the hand has two pairs of cards with
            the same rank, False otherwice.
        """
        if Counter(self.ranks.values())[2] >= 2:
            return True

        return False


    def has_three_of_kind(self):
        """
            Returns True if the hand has three cards with the same rank,
            False otherwice.
        """
        return self.has_pair(pair_count=3)


    def has_four_of_kind(self):
        """
            Returns True if the hand has four cards with the same rank,
            False otherwice.
        """
        return self.has_pair(pair_count=4)


    def has_straight(self):
        """
            Returns True if the hand has a straight,
            False otherwice.
        """
        self.cards.sort()

        for i in range(len(self.cards)-1):
            if self.cards[i].rank >= self.cards[i+1].rank:
                return False

        return True


    def has_straight_flush(self):
        """
            Returns True if the hand has a straight and a flush
            at the same time, False otherwice.
        """
        return self.has_flush() and self.has_straight()



    def has_full_house(self):
        """
            Returns True if the hand has a full house
            at the same time, False otherwice.
        """
        if 3 in self.ranks.values() and 2 in self.ranks.values():
            return True

        return False


    def classify(self):
        """
            Figures out the highest-value classification for a hand
            and sets the label attribute accordingly.
        """
        self.rank_hist()
        self.suit_hist()

        label_values = (
            "pair", "two pair", "three of a kind", "straight",\
            "flush", "full house", "four of a kind", "straight flush", '')

        classification_order = (
            self.has_pair, self.has_two_pair, self.has_three_of_kind,\
            self.has_straight, self.has_flush, self.has_full_house,\
            self.has_four_of_kind, self.has_straight_flush)

        for func in classification_order:
            if func():
                self.label = label_values[classification_order.index(func)]


    def estimate_probabilities(self, prob: int=100):
        """
            Estimates a probability of a certain amount of hands to
            have some classification.
        """
        result = {}

        for i in range(prob):
            deck = Deck()
            deck.shuffle()
            hand = PokerHand()
            deck.move_cards(hand, 7)

            hand.classify()

            result[hand.label] = result.get(hand.label, 0) + 1

        return result


def test_classification(hand) -> None:
    """
        Tests each poker hand and prints the result on it.
        Elements can either be True or False.
    """
    print(f"Hand has a flush: {hand.has_flush()}")
    print(f"Hand has a straight: {hand.has_straight()}")
    print(f"Hand has a straight flush: {hand.has_straight_flush()}")

    print(f"Hand has a pair: {hand.has_pair()}")
    print(f"Hand has a double pair: {hand.has_two_pair()}")
    print(f"Hand has a three of a kind: {hand.has_three_of_kind()}")
    print(f"Hand has a four of a king: {hand.has_four_of_kind()}")

    print(f"Hand has a full house: {hand.has_full_house()}")


def main() -> None:
    """
        The main function in the script
    """
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    #for i in range(7):
        #hand = PokerHand()
        #deck.move_cards(hand, 7)
        #hand.sort()

        #print(hand)
        #hand.classify()
        #print(hand.label, "\n")

    hand = PokerHand()
    hand.sort()

    pprint([(key, val/100000) for key, val in hand.estimate_probabilities(100000).items()])


if __name__ == '__main__':
    main()

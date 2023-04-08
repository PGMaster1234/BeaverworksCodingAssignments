import random


class Card:

    rank_to_str = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
    suit_to_str = {'C': 'Clubs', 'H': 'Hearts', 'S': 'Spades', 'D': 'Diamonds'}
    suit_to_id = {'C': 26, 'H': 39, 'S': 0, 'D': 13}

    def __init__(self, rank: int, suit: str):
        assert 2 <= rank <= 14
        assert suit.upper() in {'C', 'H', 'S', 'D'}

        self.r = rank
        self.s = suit
        self.id = Card.suit_to_id[self.s] + self.r - 1

    def __repr__(self):
        if self.r > 10:
            return str(Card.rank_to_str[self.r]) + " of " + str(Card.suit_to_str[self.s])
        else:
            return str(self.r) + " of " + str(Card.suit_to_str[self.s])

    def __lt__(self, other):
        if self.r < other.r:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.r > other.r:
            return True
        else:
            return False

    def __le__(self, other):
        if self.r <= other.r:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.r >= other.r:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.r == other.r:
            return True
        else:
            return False


c = Card(14, "H")


def create_list(r1, r2):
    lis = []
    for i in range(r2-r1 + 1):
        lis.append(r1 + i)
    return lis


class Deck:
    def __init__(self, shuffled=False):
        self.list = []
        self.dealt = 0
        self.shuffled = shuffled
        if self.shuffled:
            Deck.shuffle(self)
        else:
            self.list = create_list(1, 52)

    def shuffle(self):
        self.list = []
        unshuffled = create_list(1, 52)
        for i in range(52):
            x = unshuffled[random.randint(0, len(unshuffled) - 1)]
            self.list.append(x)
            unshuffled.remove(x)

    def deal_card(self):
        if len(self.list) > 0:
            top_card = self.list[0]
            self.list.remove(self.list[0])
            return top_card
        else:
            return None

    def __repr__(self):
        return self.dealt, self.shuffled, self

    def reset(self):
        self.shuffled = False
        self.list = create_list(1, 52)
        self.dealt = 0


d = Deck(shuffled=True)
d.reset()
# Do not change import statements.
import unittest
from SI507F17_project1_cards import *
from helper_functions import *


class CardsTestCase(unittest.TestCase):

    def setUp(self):
        self.Card = Card()
        self.Card1 = Card(1, 13)

    def tearDown(self):
        self.Card = None
        self.Card1 = None

    def test_Card_Suit_Names(self):
        self.assertEqual(self.Card.suit_names, [
                         "Diamonds", "Clubs", "Hearts", "Spades"])

    def test_Card_Rank_Levels(self):
        self.assertEqual(self.Card.rank_levels, list(range(1, 14)))

    def test_Card_Faces(self):
        self.assertEqual(self.Card.faces, {
                         1: "Ace", 11: "Jack", 12: "Queen", 13: "King"})

    def test_Card_Constructor(self):
        self.assertEqual(self.Card.suit, "Diamonds")
        self.assertEqual(self.Card.rank, 2)
        self.assertEqual(self.Card.rank_num, 2)
        self.assertEqual(self.Card1.suit, "Clubs")
        self.assertEqual(self.Card1.rank, "King")
        self.assertEqual(self.Card1.rank_num, 13)

    def test_Card_String(self):
        self.assertEqual(str(self.Card), "2 of Diamonds")
        self.assertEqual(str(self.Card1), "King of Clubs")


class DeckTestCase(unittest.TestCase):

    def setUp(self):
        self.Deck = Deck()
        self.Card = Card()

    def tearDown(self):
        self.Deck = None
        self.Card = None

    def test_Deck_Constructor(self):
        test_Deck = []
        for suit in range(4):
            for rank in range(1, 14):
                test_Deck.append(Card(suit, rank))
        for i in range(52):
            self.assertEqual(self.Deck.cards[i].suit, test_Deck[i].suit)
            self.assertEqual(
                self.Deck.cards[i].rank_num, test_Deck[i].rank_num)

    def test_Deck_String(self):
        discription = ['2', '3', '4', '5', '6', '7', '8',
                       '9', '10', "Jack", "Queen", "King", "Ace"]
        outPrints = str(self.Deck).split("\n")
        self.assertEqual(len(outPrints), 52)
        for line in outPrints:
            word = line.split()
            self.assertIn(word[0], discription)
            self.assertIn(word[2], self.Card.suit_names)

    def test_Deck_Pop_Card(self):
        for i in range(52):
            self.assertIsInstance(self.Deck.pop_card(), Card)
            self.assertEqual(len(self.Deck.cards), 51-i)
        self.assertEqual(len(self.Deck.cards), 0)

    def test_Deck_Shuffle(self):
        orderedPrint = str(self.Deck).split('\n')
        self.Deck.shuffle()
        newPrint = str(self.Deck).split('\n')
        self.assertNotEqual(orderedPrint, newPrint)

    def test_Deck_Replace_Card(self):
        while len(self.Deck.cards) != 0:
            self.Deck.pop_card()
        Ace_of_Sapdes = Card(3, 1)
        self.Deck.replace_card(Ace_of_Sapdes)
        self.assertEqual(len(self.Deck.cards), 1)
        self.Deck.replace_card(Ace_of_Sapdes)
        self.assertEqual(len(self.Deck.cards), 1)

    def test_Deck_Sort_Cards(self):
        orderedPrint = str(self.Deck).split('\n')
        self.Deck.shuffle()
        self.Deck.sort_cards()
        sortedPrint = str(self.Deck).split('\n')
        self.assertEqual(orderedPrint, sortedPrint)

    def test_Deck_Sort_Partial_Cards(self):
        for _ in range(13):
            self.Deck.pop_card(0)
        orderedPrint = str(self.Deck)
        self.Deck.shuffle()
        self.Deck.sort_cards()
        sortedPrint = str(self.Deck).split('\n')
        self.assertEqual(orderedPrint, sortedPrint)

    def test_Deck_Deal_Hand(self):
        for i in range(3):
            self.Deck.pop_card()
        print(len(self.Deck.cards))
        # for a deck of 49 cards, if the handsize is bigger than 25, the
        # deal_hand malfunctions.
        self.assertEqual(len(self.Deck.deal_hand(49)), 49)


class play_War_GameTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Play(self):
        num_str = 0
        num_int = 0
        self.assertIsInstance(play_war_game(True), tuple)
        self.assertEqual(len(play_war_game(True)), 3)
        for i in play_war_game(True):
            if type(i) == str:
                self.assertIn(i, ("Player1", "Player2", "Tie"))
                num_str += 1
            if type(i) == int:
                num_int += 1
            else:
                continue
        self.assertEqual(num_str, 1)
        self.assertEqual(num_int, 2)

class play_GameTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDowm(self):
        pass

    def test_play(self):
        play_game()

class show_SongTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Show_Song(self):
        s = show_song()
        self.assertIsInstance(s, Song)
        # print(s)
        s1 = show_song('Bowie')
        self.assertIsInstance(s1, Song)
        self.assertFalse('Bowie' in str(s1))


if __name__ == '__main__':
    unittest.main(verbosity=2)


# Write your unit tests to test the cards code here.
# You should test to ensure that everything explained in the code description file works as that file says.
# If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
# You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
# You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########

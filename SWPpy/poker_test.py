import unittest
import array
import pokersimulation as poker
class PokerTest(unittest.TestCase):

    # methode for testing card taking
    def test_get_cards(self):
        choise = poker.take_cards(5)
        self.assertEqual(len(choise), 5, 'incorrect length')

    # test pair
    def test_pair(self):
        cards1 = [0,2,3,2,8]
        cards2 = [12,1,5,0,10]
        self.assertEqual(poker.check_equal_cards(cards1,2), True,
                         'incorrect check_equal function')
        self.assertEqual(poker.check_equal_cards(cards2, 2), False,
                         'incorrect check_equal function')

    # test straight
    def test_straight(self):
        cards1 = [2,3,5,6,4]
        cards2 = [0,11,10,9,12]
        cards3 = [3,12,5,6,7]
        self.assertEqual(poker.check_straight(cards1), True,
                         'incorrect check_straight func')
        self.assertEqual(poker.check_straight(cards2), True,
                         'incorrect straight - 0-12')
        self.assertEqual(poker.check_straight(cards3), False,
                         'incorrect check_straight func')

    # test royal flush
    def test_royal(self):
        cards1 = [3,1,2,5,3]
        cards2 = [12,10,11,9,0]
        self.assertEqual(poker.check_royalflush(cards1), False,
                         'incorrect royal flush func')
        self.assertEqual(poker.check_royalflush(cards2), True,
                         'incorrect royal flush func')


if __name__ == '__main__':
    unittest.main()

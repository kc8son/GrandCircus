import unittest
import main


class MyTestCase(unittest.TestCase):
    ####################################################################################################
    #   Straight - three tests
    def test_check_straight001(self):
        self.assertEqual(main.check_straight("s3", "s2", "s1"), 3)

    def test_check_straight002(self):
        self.assertEqual(main.check_straight("sa", "sk", "sq"), 14)

    def test_check_straight003(self):
        self.assertEqual(main.check_straight("s10", "sj", "sq"), 12)

    ####################################################################################################
    #   3 of a kind - four tests
    def test_check_3ofa_kind001(self):
        self.assertEqual(main.check_straight("s5", "s5", "s5"), 5)

    def test_check_3ofa_kind002(self):
        self.assertEqual(main.check_3ofa_kind("sq", "sq", "sq"), 12)

    def test_check_3ofa_kind003(self):
        self.assertEqual(main.check_3ofa_kind("sa", "sa", "sa"), 14)

    def test_check_3ofa_kind004(self):
        self.assertEqual(main.check_3ofa_kind("sa", "sq", "sq"), 0)

    def test_check_3ofa_kind005(self):
        self.assertEqual(main.check_3ofa_kind("sq", "sq", "sa"), 0)

    ####################################################################################################
    #   Royal Flush - 3 tests
    def check_royal_flush001(self):
        self.assertEqual(main.check_royal_flush("sa", "sq", "sk"), 14)
    def check_royal_flush002(self):
        self.assertEqual(main.check_royal_flush("sq", "sq", "sa"), 0)
    def check_royal_flush003(self):
        self.assertEqual(main.check_royal_flush("sq", "sk", "sj"), 0)

    ####################################################################################################
    #   Play Cards - 9 tests
    def check_play_cards001(self):
        self.assertEqual(main.play_cards("sa", "sq", "sk", "sq", "sk", "sj"), -1) # test straights
    def check_play_cards002(self):
        self.assertEqual(main.play_cards("sq", "sk", "sj", "sa", "sq", "sk"), 1)
    def check_play_cards003(self):
        self.assertEqual(main.play_cards("sa", "sq", "sk", "sa", "sq", "sk"), 0)

    def check_play_cards004(self):
        self.assertEqual(main.play_cards("sa", "sq", "sk", "s5", "s5", "s5"), -1) # Test 3 of a kind
    def check_play_cards005(self):
        self.assertEqual(main.play_cards("s5", "s5", "s5", "sa", "sq", "sk"), 1)
    def check_play_cards006(self):
        self.assertEqual(main.play_cards("s5", "s5", "s5", "s5", "s5", "s5"), 0)

    def check_play_cards007(self):
        self.assertEqual(main.play_cards("s3", "s2", "s1", "s10", "sj", "sq"), 1) # straight
    def check_play_cards008(self):
        self.assertEqual(main.play_cards("s10", "sj", "sq", "s3", "s2", "s1"), -1)
    def check_play_cards009(self):
        self.assertEqual(main.play_cards("s3", "s2", "s1", "s3", "s2", "s1"), 0)

if __name__ == '__main__':
    unittest.main()

# #   factorial..
# def fact(x):
#     """Return x!"""
#     if x < 1:
#         return 0
#     if x == 0:
#         return 1
#     else:
#         result = 1
#         for num in range(1, x+1):
#             result = result * num
#         return result
#         # return(fact(x-1)0
# print(fact(0))
# print(fact(1))
# print(fact(2))
# print(fact(4))

import unittest
import practice
print(practice.get_sign(-5))

class MyTestCase(unittest.TestCase):
    def test_get_sign_neg5(self):
        self.assertEqual(practice.get_sign(-5), -1)
    def test_get_sign_pos5(self):
        self.assertEqual(practice.get_sign(5), 1)
    def test_get_sign_0(self):
        self.assertEqual(practice.get_sign(0), 0)
    def test_get_sign_one(self):
        self.assertEqual(practice.get_sign(1), 1)

if __name__ == '__main__':
    unittest.main()


python -m unittest main_test.py

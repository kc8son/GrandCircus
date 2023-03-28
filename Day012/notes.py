# # import numpy as np
# #
# # class LinearRegression:
# #     def __init__(self):
# #         self.coef_ = None
# #         self.intercept_ = None
# #
# #     def fit (self, x, y):
# #         X = np.array(X)
# #         y = np.array(y)
# #         n = X.shape[0]  # number of rows in X...
# #         x_mean = np.mean(X)
# #         y_mean = np.mean(y)
# #
# #         numerator = 0
# #         denominator = 0
# #
# #
# # a1 = LinearRegression()
# # print(a1.coef_)
# # print(a1.intercept_)
#
#
# #   part 2...
# class Pen:
#     def __init__(self):
#         self.color = ''
#         self.length = ''
#         self.point_type = ''
#         self.ink_amount = 0
#
#     def draw(self):
#         self.ink_amount -= 1
#
#     def refill(self):
#         self.ink_amount = 10
#
# p1 = Pen()
# print(p1.ink_amount)
# p1.ink_amount = 5
# print(p1.ink_amount)
# p1.draw()
# print(p1.ink_amount)
# p1.refill()
# print(p1.ink_amount)
#
#
#
# p2 = Pen()
# print(p2.ink_amount)
# p2.ink_amount = 7
# print(p2.ink_amount)
#


class Pen:
    number_instances = 0    #variable across all instanes...  class variable (as opposed to member variable)
    def __init__(self):
        self.ink_color = init_color
        self.length =
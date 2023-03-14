# #   filter...
# nums = [2, 208, 5, 7, 800, 1000, 3]
#
# def isbig(num):
#     return num >= 100
#
# bignums = list(filter, nums)
# print(bignums)
#
# bignums2 = list(filter(lambda x: x >= 100, nums))
#
#
# #   MAP...
# nums  [3, 4, 10, 15]

# research difference between map & filter...  filter might reduce the number of elements returned.


#   Today's main topic:  Tuples and dictionaries...
# list = [] - mutable
# tuple = () - immutable - less memory and a little faster
# dictionary = {} - k/v pairs
#
# bon = (5, 10, 1, 2)
# print(bon)
#
# more_tuple_elements = ('good', 'bad')
# print(more_tuple_elements)
#
# more_tuple_elements2 = ('good', 'bad', 5, 10, 1, 2)
# for ele in more_tuple_elements2:
#     print(ele, ele*2)

# #   che k if an element exists...
# colors = ('red', 'green', 'blue')
# if 'blue' in colors:
#     print('yup - blue')
# if 'orange' not in colors:
#     print('no orange')

# some_colors = ('red', 'green', 'blue', 'yellow')
# more_colors = ('purple', 'orange', 'cyan')
# all_colors = some_colors+more_colors
# print(all_colors)
# #   The ELEMENTS are immutable
# print('before:', some_colors)
# some_colors = some_colors+more_colors
# print('after:', some_colors)

# #   A tuple must have more than one element...
# one_element_tuple = (5)
# print(type(one_element_tuple))
#
# two_element_tuple = (5, 8)
# print(type(two_element_tuple))
#
# #force to tuple
# one_element_tuple2 = (5,)
# print(type(one_element_tuple2))
# print(len(one_element_tuple2))

# # indexing...
# all_colors = ('red', 'green', 'blue', 'yellow', 'purple', 'orange', 'cyan')
# print(all_colors[2:6])
# print(type(all_colors[2:6]))

# #   Dictionary: key, value pairs
# grades = {
#     'Fred': 90,
#     "Sally": 100,
#     "Abdul": 76,
#     "julia": 85,
#     "Samuel": 89
# }
#
# #   index by value
# print("before: ", grades["julia"])
# grades["julia"] = 110
# print("before: ", grades["julia"])
# print(len(grades))
# #   Can't reference by index nuber.  Have to use the key.
# #print(grades[0])
#
# stuff = {
#     "hello": "world",
#     10: "greeting",
#     5.5: "and",
#     True: 11.6
# }
# print(stuff["hello"])
# print(stuff[10])
# print(stuff[5.5])
# print(stuff[True])
#
#
# print("="*50)
# for ele in stuff:
#     print(ele, stuff[ele])
#
# # #   Doesn't work...
# # print("="*50)
# # for k, v in stuff:
# #     print(k, v)


# grades = {
#     'Fred': 90,
#     "Sally": 100,
#     "Abdul": 76,
#     "julia": 85,
#     "Samuel": 89
# }
# print("before:", grades)
# del grades["Fred"]
# print("after:", grades)
# # grades.clear()
# # print("again:", grades)
# if "Abdul" in grades:   # check for key
#     print("found")

#   comvining dictionaries
grades1 = {
    'Fred': 90,
    "Sally": 100,
    "Abdul": 76,
    "julia": 85,
    "Samuel": 89
}
grades2= {
    'Fred': 90,
    "Joe": 100,
    "Able": 76,
    "Baker": 85,
    "Charlie": 89
}

all_grades = grades1 | grades2
print(all_grades)
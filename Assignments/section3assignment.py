# Assignment 1:
"""
    Create a function named merge_lists that accepts 2 lists.
    The function is supposed to merge both of those lists together
    and return the result.
"""

# your code below:

# solution Below:

# def merge_lists(list_a, list_b):
#     return list_a + list_b
#
# my_list = merge_lists([1,2,3],['a', 'b', 'c'])
# print(my_list)



# Assignment 2:
"""
    create a function called separate() that accepts a string as an argument
    and returns a list containing each of the characters of
    the string separated as individual items in the list.

    Make sure to test the function.
"""
# Your Code Below:

# Solution Below:

# def separate(str):
#     return list(str)
#
# print(separate("hello there"))



# Assignment 3:
"""
Create a function called multi_merge that takes a list and a string
as arguments.

The function is supposed to return a merged list
containing the original list argument as well as each of the words that are in
the string argument in addition to each of the characters in the string
argument as individual elements in the list.

"""
# Your Code Below:

# Solution:

# def multi_merge(list_a, str):
#     return list_a + str.split() + list(str)
#
# print(multi_merge([1,2,3,4], "Hello My name is imtiaz"))



# Assignment 4:
"""
Define a function called last_list that can accept an unlimited number
of lists but returns only the last list.

Example:

    For example, the below function call should return ['mike', 'john']

    last_list([1,2,3,4,5], ['a', 'b', 'c'], ['mike', 'john'])

"""

# Your code below:

# Solution:

# def last_list(*args):
#     return args[-1 :len(args)]



# Assignment 5:
"""
Define a function called key_list_items that can accept an unlimited number
of lists along with another argument. The function should return
the second_folder to last item in the specific list specified by the user of the function.

Example:

    For example, the below function call should return: jan

    key_list_items("people", things=['book', 'tv'], people=['pete', 'mike', 'jan', 'tom'])

"""

# Your Code Below:

# Solution:

# def key_list_items(key, **kwargs):
#     keys = kwargs[key]
#     return keys[-2]
#
# result = key_list_items("people", things=['book', 'tv', 'shoes'], people=['pete', 'mike', 'jan', 'tom'],
#                 ages=[20, 30, 40])
# print(result)
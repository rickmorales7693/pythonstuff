# Assignment 1

"""

Create a method called twelver that accepts 2 integer arguments: a and b.
The method should return True if one of the arguments is 12
or if the sum of both arguments equals 12.

twelver(3, 12) → True
twelver(4, 9) → False
twelver(9, 3) → True

"""

# Your Code Below:

# Solution:
# def twelver(a, b):
#   return (a == 12 or b == 12 or a+b == 12)



# Assignment 2
"""
Create a method called pay_extra that accepts 2 parameters:
 working, and hour. This method will be used to decide whether
 an employee will receive extra pay or not. If an employee is working
 during the hrs of 8pm until 8am in the morning, that means they
 should be paid extra. In that situation the method should return true,
 otherwise it should return false.

 NOTE: the hour parameter should be from 0-23.
        So 8AM is hour 8, and 8PM is hour 20.

Example:
    pay_extra(True, 11) -> false
    pay_extra(False, 5) -> false
    pay_extra(True, 6)  -> true
"""

# Your Code Below:

# Solution
# def pay_extra(working, hour):
#     return (working and (hour < 8 or hour > 20))



# Assignment 3
"""
Given a list of ints, return True if the sequence of numbers 1, 2, 3
appears in the list anywhere, false otherwise.

sequence([1, 1, 2, 3, 1]) → True
sequence([1, 1, 2, 4, 1]) → False
sequence([1, 1, 2, 1, 2, 3]) → True
sequence([1, 2]) → False
sequence([]) → False
"""

# Your Code Below:

# Solution:

# def sequence(num_list):
#     # Note: iterate with length-2, so can use i+1 and i+2 in the loop
#     for i in range(len(num_list) - 2):
#         if num_list[i] == 1 and num_list[i + 1] == 2 and num_list[i + 2] == 3:
#             return True
#     return False



# Assignment 4
"""
Given a non-empty string like "Code" return a string like "CCoCodCode".

grow_string('Code') → 'CCoCodCode'
grow_string('abc') → 'aababc'
grow_string('ab') → 'aab'

"""

# Your Code Below:

# Solution:

# def grow_string(str):
#   result = ""
#   # On each iteration, add the substring of the chars 0..i
#   for i in range(len(str)):
#     result = result + str[:i+1]
#   return result



# Assignment 5
"""
Define a method that accepts a list as an argument
and returns True if one of the first_folder 4 elements
in the list is a 6. The list length may be less than 4.


first3([1, 2, 6, 3, 4]) → True
first3([1, 2, 3, 4, 6]) → False
first3([1, 2, 3, 4, 5]) → False

"""

# Your Code Below:







print(first3([1,2,6,3,0,0])) # true
print(first3([1,2,3,3,0,6])) # false
print(first3([6])) # true
print(first3([])) # false

# Solution:

# def first3(numbers):
#     # First figure the end for the loop
#     end = len(numbers)
#     if end > 4:
#         end = 4
#
#     for i in range(end):  # loop over index [0, 1, 2, 3]
#         if numbers[i] == 6:
#             return True
#     return False



# Assignment 6
"""
Create a function called last2 that accepts a string argument.
The function should return the count of the number of times that the last
2 characters appear in the rest of the string. You should not count
the last 2 characters as an occurrence. The last 2 characters is just the
sequence your function should look for in the remaining string.

So "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2

"""

# Your Code Below:



print(last2('hixxhi')) #→ 1
print(last2('xaxxaxaxx')) #→ 1
print(last2('axxxxaaxx')) #→ 3

# Solution

# def last2(str):
#     # Screen out too-short string case.
#     if len(str) < 2:
#         return 0
#
#     # last 2 chars, can be written as str[-2:]
#     last2 = str[len(str) - 2:]
#     count = 0
#
#     # Check each substring length 2 starting at i
#     for i in range(len(str) - 2):
#         sub = str[i:i + 2]
#         if sub == last2:
#             count = count + 1
#
#     return count



# Assignment 7
"""
Given 2 strings, a and b, return the number of the positions where
they contain the same length 2 substring. So "xxcaazz" and "xxbaaz"
yields 3, since the "xx", "aa", and "az" substrings appear in the same
place in both strings.

EXAMPLE:
    string_match('xxcaazz', 'xxbaaz') → 3
    string_match('abc', 'abc') → 2
    string_match('abc', 'axc') → 0

"""

#Your Code Below:

# Solution
# def string_match(a, b):
#     # Figure which string is shorter.
#     shorter = min(len(a), len(b))
#     count = 0
#
#     # Loop i over every substring starting spot.
#     # Use length-1 here, so can use char str[i+1] in the loop
#     for i in range(shorter - 1):
#         a_sub = a[i:i + 2]
#         b_sub = b[i:i + 2]
#         if a_sub == b_sub:
#             count = count + 1
#
#     return count



# Assignment 8
"""

Return the sum of the numbers in the list, except ignore sections of
numbers starting with a 7 and extending to the next 8
(every 7 will be followed by at least one 8).
Return 0 for no numbers.

EXAMPLE:
sum78([1, 2, 2]) → 5
sum78([1, 2, 2, 7, 99, 99, 8]) → 5
sum78([1, 1, 7, 8, 2]) → 4

"""

#Your Code Below:


print(sum78([1, 2, 2])) #→ 5
print(sum78([1, 2, 2, 7, 99, 99, 8])) #→ 5
print(sum78([1, 1, 7, 8, 2])) #→ 4

# Solution:

# def sum78(nums):
#     sum = 0
#     inRange = False
#
#     for i in range(len(nums)):
#         if nums[i] == 7:
#             inRange = True
#
#         if not inRange:
#             sum += nums[i]
#
#         if inRange and nums[i] == 8:
#             inRange = False
#
#     return sum



# Assignment 9
"""
We have 2 variables. fr and d. fr is a list of strings and d is a dictionary with email
addresses as keys and numbers as values (numbers in string format).
Write code to replace the email address in each of the strings in the fr list with
the associated value of that email looked up from the dictionary d.
If the dictionary does not contain the email found in the list, add a new entry
in the dictionary for the email found in the fr list. The value for this new email key
will be the next highest value number in the dictionary in string format.

Once the dictionary is populated with this new email key and a new number value,
replace that email's occurrence in the fr list with the number value.

The output of running your completed code should be the following:

Value of fr:
['199|4|11|GDSPV', '199|16|82|GDSPV', '205|12|82|GDSPV', '206|19|82|GDSPV']
Value of d:
{'7@comp1.COM': '199', '8@comp4.COM': '200', '13@comp1.COM': '205', '26@comp1.COM': '206'}

"""

# Don't manually change fr and d.
fr = [
'7@comp1.COM|4|11|GDSPV',
'7@comp1.COM|16|82|GDSPV',
'13@comp1.COM|12|82|GDSPV',
'26@comp1.COM|19|82|GDSPV'
]

d= {
'7@comp1.COM': '199',
'8@comp4.COM': '200',
'13@comp1.COM': '205'
}


# Your Code Below:
# --------------------------------------



# don't change the lines below:
# --------------------------------------
print("Value of fr: ")
print(fr)
print("Value of d:")
print(d)

# Solution:
#
# line_list = []
# # this won't work for missing keys
# for line in fr:
#     columns = line.split("|")
#     lookup_val = columns[0]
#
#     # if lookup_val not in d.keys():
#     if(d.get(lookup_val) is None): # Can't find in dict
#
#         # get the next number + 1 from dict
#         next_number = int(max(d.values())) + 1
#         d[lookup_val] = str(next_number)
#         columns[0] = str(next_number)
#         line_list.append("|".join(columns))
#     else:
#         columns[0] = d.get(columns[0])
#         line_list.append("|".join(columns))
#
# fr = line_list
#
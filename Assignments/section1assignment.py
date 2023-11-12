# Assignment 1:
"""
    We would like to get the remainder of 15 divided by 4.
    The calculation below does not seem to give us this result.
    How would you change the code to meet the requirement?
"""
# Solution:
remainder = "The remainder is {0}".format(15 % 4)
print(remainder)



# Assignment 2:
"""
Use of the below format() method is incorrect for what we are trying to do.
We actually have 10 small, 12 large, and 12 medium boxes.
Write code to correct this:


print("We have {2} small boxes, {2} large boxes, {2} medium boxes".format(10,12,12))

"""
# Solution:
print("We have {0} small boxes, {1} large boxes, {2} medium boxes".format(10, 12, 12))



# Assignment 3:
"""
    Given 2 variables chars and word, write code to move
    the data contained in the variable word in the exact middle of
    the characters contained in the variable chars and save this
    in a new variable called result and print it.

    NOTE: chars variable will contain only 4 characters

    Example:
    ---------------
    chars = "<<>>"
    word = "hello"
    result - should contain the following string: <<hello>>

"""

chars = "[[]]"
word = "Cool"

# Expected Result Printed: [[Cool]]

# Your code below:
print(chars[:2] + word + chars[2:])



# Assignment 4:
"""
    Given 2 variables word1 and word2, write code to
    print the concatenation of the 2 words omitting the
    first_folder letter of the string saved in word1 and the second_folder
    letter of the string saved in word2.

    Example:
    ---------------
    word1 = "Vehicle"
    word2 = "Robot"
    result - VehicleRobot

"""

word1 = "Computer"
word2 = "Truck"

# Expected Result Printed: ComputerTuck

# Your code below:
result = word1[0:] + word2[0:1] + word2[2:]
print(result)



# Assignment 5:
"""
    Given 2 variables chars and word, write code to move
    the data contained in the variable word in the exact middle of
    the characters contained in the variable chars and save this
    in a new variable called result and print it.

    NOTE: chars variable can contain any even number of characters.
          the len() function can be used to figure out the length of a string

    Example:
    ---------------
    chars = "<[<||>]>"
    word = "mirror"
    result - should contain the following string: <[<|mirror|>]>

"""

chars = "<<[]]]" # this could be a very long string with an even length.
word = "Cool"

# Expected Result Printed: <<[Cool]]]

# Your code below:
size = len(chars)
idx = int(size/2) # dividing results in a float datatype.
print(chars[:idx] + word + chars[idx:])
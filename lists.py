my_list = [1, 2, 3, 4, 5]

my_list.pop()  # removes the last item in the list
print(my_list)

my_list.pop(0)  # removes the first item in the list
print(my_list)

my_list[0] = 0  # replaces the first item in the list
print(my_list)

my_list.append(6)  # adds an item to the end of the list
print(my_list)

my_list.append([7, 8, 9])
print(my_list)

my_list = ['a', 'b', 'c', 'd', 'e']
my_list.sort()  # sorts the list in ascending order even if it is a string
print(my_list)
print(my_list[-1])  # prints the last item in the list

item_count = len(my_list)  # returns the length of the list
print(item_count)

my_list = [1, 2, 3, 4, 5]
another_list = [6, 7, 8, 9, 10]
new_list = my_list + another_list  # concatenates the two lists
print(new_list)

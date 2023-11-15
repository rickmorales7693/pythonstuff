my_list = ['b', 'd', 'a', 'z', 'x']
another_list = [1, 2, 3, 4, 5]

#  needs to look like this ['d', 'b', 'a', 3, 2, 1]

my_list.sort()
my_list.reverse()

another_list.reverse()

final_list = my_list[2:] + another_list[2:]

print(final_list)
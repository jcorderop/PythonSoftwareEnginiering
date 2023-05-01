
# List Compression
list1 = [I for I in range(5) if (I < 3)]
print('filtering compression {}'.format(list1))

list2 = [I if I > 2 else -1 for I in range(5)]
print('changing compression {}'.format(list2))

# merging dict
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3}
dict3 = {**dict1, **dict2}
print(dict3)

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3}
dict3 = dict1 | dict2
print(dict3)



# Tuple Packing & Unpaking
# Use _ to drop single values
x, y, _ = (1, 2, 3)
print('x {}, y {}'.format(x, y))
# Use * to drop multiple variables
x, y, *my_list = (1, 2, 3, 4, 5, 6, 7)
print('x {}, y {}'.format(x, y))
print('the rest: {}'.format(my_list))






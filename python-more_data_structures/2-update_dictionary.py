def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value

# Example Usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}
update_dictionary(my_dict, 'b', 10)  # Replace 'b' with 10
update_dictionary(my_dict, 'd', 4)   # Add 'd' with value 4

print(my_dict)
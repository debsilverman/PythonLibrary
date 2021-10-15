# we have two lists in Python, and we want to merge them in a dictionary form, 
# where one list's items act as the dictionary's keys and the other's as the values.
# we need to consider a couple of restrictions, such as the sizes of the two lists, 
# the types of items in the two lists, and if there are any repeated items in them, 
# especially in the one we will use as keys. We can overcome that with the use of 
# built-in functions like zip

keys_list = ['A', 'B', 'C']
values_list = ['blue', 'red', 'bold']

#There are 3 ways to convert these two lists into a dictionary
#1- Using Python's zip, dict functionz
dict_method_1 = dict(zip(keys_list, values_list))

#2- Using the zip function with dictionary comprehensions
dict_method_2 = {key:value for key, value in zip(keys_list, values_list)}

#3- Using the zip function with a loop
items_tuples = zip(keys_list, values_list) 
dict_method_3 = {} 
for key, value in items_tuples: 
    if key in dict_method_3: 
        pass # To avoid repeating keys.
    else: 
        dict_method_3[key] = value
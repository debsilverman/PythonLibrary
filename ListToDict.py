# if we are given a list and map it into a dictionary. 
# That is, I want to convert my list into a dictionary with numerical keys
mylist = ['blue', 'orange', 'green']
#Map the list into a dict using the map, zip and dict functions
mapped_dict = dict(zip(itr, map(fn, itr)))
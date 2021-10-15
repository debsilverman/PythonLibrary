# Depending on the data type of the items included in the lists, 
# we will follow a slightly different way to sort them. 
# LThis example is sorting a list of dictionaries
dicts_lists = [
  {
    "Name": "James",
    "Age": 20,
  },
  {
     "Name": "May",
     "Age": 14,
  },
  {
    "Name": "Katy",
    "Age": 23,
  }
]

#There are different ways to sort that list
#1- Using the sort/ sorted function based on the age
dicts_lists.sort(key=lambda item: item.get("Age"))

#2- Using itemgetter module based on name
from operator import itemgetter
f = itemgetter('Name')
dicts_lists.sort(key=f)
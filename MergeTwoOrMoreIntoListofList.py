# we have two or more lists, and we want to collect them all in one big list of lists, 
# where all the first items of the smaller list form the first list in the bigger list.
# For example, if I have 4 lists [1,2,3], [‘a’,’b’,’c’], [‘h’,’e’,’y’], 
# and [4,5,6] and we want to make a new list of those four lists; 
# it will be [[1,’a’,’h’,4], [2,’b’,’e’,5], [3,’c’,’y’,6]] .

def merge(*args, missing_val = None):
#missing_val will be used when one of the smaller lists is shorter tham the others.
#Get the maximum length within the smaller lists.
  max_length = max([len(lst) for lst in args])
  outList = []
  for i in range(max_length):
    result.append([args[k][i] if i < len(args[k]) else missing_val for k in range(len(args))])
  return outList
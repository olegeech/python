# python

def linear_search(a_list, target):
  for element in a_list:
    if element == target:
      return TRUE
  return FALSE


def binary_search(a_list, target=1):
  # sort list ascending by num or ...
  a_list = [0, 1, 2, 3, 4, 5]
  low = 0
  high = len(a_list) #6, 
  while (low + 1 < high): #1<6:TRUE, 1<3:TRUE; 3<3:FALSE
    test = (low + high)/2 #0+6/2=3, 0+3/2=2
    if (a_list[test] > target): #2>1:TRUE, 1>1:FALSE
      high = test #3
    #elif a_list[test] == target:
      #return TRUE
    else:
      low = test #2
  if (a_list[low] == target): #1 == 1:TRUE
    return TRUE
  else:
    return FALSE
  
  
  
  list_size = len(a_list)
  mid_list_element = list_size/2
  if mid_list_element > target:
    ...
  if mid_list_element <= target:
    

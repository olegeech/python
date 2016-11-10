# python

a_list = [5, 8, 11, 3, 45]

def bubble_sort(lst): 
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[j] < lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
    return lst
  
  bubble_sort(a_list)


a_list = [5, 8, 11, 3, 45]


def insertion_sort(lst):
    for i in range(len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1
    return lst

print(insertion_sort(a_list))
  

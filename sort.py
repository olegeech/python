# python

a_list = [5, 8, 11, 3, 45, 1, 1.1, 4, 6, 28, 111, 2, 33, 444, 5556, 77889, 9900, "re", "weq"]

def insertion_sort(lst):
    for i in range(len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1
    return lst
print(insertion_sort(a_list))


def bubble_sort(lst): 
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[j] < lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
    return lst
  
  bubble_sort(a_list)
  

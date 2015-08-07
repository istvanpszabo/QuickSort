__author__ = 'iszabo'

def partition(l):
    length = len(l)
    pivot = l[length-1]
    left = []
    right = []

    for i in range(length-1):
        el = l[i]
        if el <= pivot:
            left += [el]
        else:
            right += [el]
    return (left, pivot, right)

def quicksort(list):
    if len(list) <= 1:
        return list
    else:
        (left, pivot, right) = partition(list)
        sorted_left = quicksort(left)
        sorted_right = quicksort(right)
        return sorted_left + [pivot] + sorted_right

print(quicksort([1, -1, 7, -3]))
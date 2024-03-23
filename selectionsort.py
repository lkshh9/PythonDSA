l = list(range(5,0,-1))

# Selection Sort algorithm,repeatedly selects the minimum element from the unsorted portion of the list and places 
# it at the beginning of the sorted portion

def SelectionSort(l):
    for start in range(0, len(l)):
        minpos = start
        for i in range(start, len(l)):
            if l[i] < l[minpos] :
                minpos = i
            (l[start], l[minpos]) = (l[minpos], l[start])
    return l

print(SelectionSort(l))

# Best Case:

# The best-case scenario for selection sort occurs when the input list is already sorted.
# In this case, the algorithm still needs to iterate over each element in the list to verify that it's 
# the minimum element and to perform the necessary swaps.
# Therefore, the best-case time complexity of selection sort is O(n^2), where n is the number of elements in the list.

# Worst Case:

# The worst-case scenario for selection sort occurs when the input list is in reverse sorted order.
# In this case, for each iteration of the outer loop, the algorithm needs to find the minimum element in the unsorted portion 
# of the list, which requires comparing each element.
# This results in n iterations of the outer loop, with n comparisons in each iteration.
# Therefore, the worst-case time complexity of selection sort is also O(n^2).

# Average Case:

# The average-case time complexity of selection sort is also O(n^2).
# This is because, regardless of the initial order of the elements, selection sort performs the same number of comparisons 
# and swaps for each pair of elements in the list.
# The number of comparisons and swaps is proportional to n^2, where n is the number of elements in the list.
# In summary, the time complexity of selection sort is O(n^2) in all cases: best-case, worst-case, and average-case. 
# This makes selection sort inefficient for large lists, especially when compared to more efficient sorting algorithms like merge sort or quick sort.
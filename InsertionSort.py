'''
Insertion sort
    Start building a sorted sequence with one element
    Pick up next sorted element and insert it into its correct place in the already sorted sequence


'''

l = [58, 42, 63, 12]

def InsertionSort(seq):
    for sliceEnd in range(len(seq)):
        pos = sliceEnd
        while pos > 0 and seq[pos] < seq[pos - 1] :
            (seq[pos], seq[pos - 1]) = (seq[pos - 1], seq[pos])
            pos = pos - 1

    return seq

print(InsertionSort(l))


'''
 for sliceEnd in range(len(seq)):
This line starts a loop that iterates over each index sliceEnd in the range from 0 to the length of the sequence seq.
The purpose of this loop is to consider each element of the sequence as the end of a sorted slice.

        pos = sliceEnd        
Within the loop, this line initializes a variable pos to the current index sliceEnd.
This variable keeps track of the position where the current element will be inserted in the sorted portion of the sequence.

        while pos > 0 and seq[pos] < seq[pos - 1]:
This line starts a while loop that continues as long as the current position pos is greater than 0 (to prevent indexing out of bounds) 
and the element at the current position seq[pos] is less than the element before it seq[pos - 1].
This loop iterates backwards through the sorted portion of the sequence, shifting elements to the right until the correct position 
for the current element is found.

            (seq[pos], seq[pos - 1]) = (seq[pos - 1], seq[pos])
Within the while loop, this line swaps the current element with the element before it.
This effectively inserts the current element into its correct position in the sorted portion of the sequence.

            pos = pos - 1
After swapping the elements, this line decrements the position pos to continue iterating backwards through the sorted portion of the sequence.
'''

'''
Best Case:

The best-case scenario for Insertion Sort occurs when the input list is already sorted.
In this case, for each element in the list, the algorithm only needs to compare it with the element before it (or none at all) to 
determine its correct position in the sorted portion of the list.
Therefore, in the best-case scenario, the time complexity of Insertion Sort is O(n), where n is the number of elements in the list.

Worst Case:

The worst-case scenario for Insertion Sort occurs when the input list is in reverse sorted order.
In this case, each element needs to be compared with and possibly swapped with every preceding element in the list to reach its 
correct position.
This results in approximately n^2/2 comparisons and swaps.
Therefore, in the worst-case scenario, the time complexity of Insertion Sort is O(n^2).

Average Case:

The average-case time complexity of Insertion Sort is also O(n^2).
This is because, on average, each element will need to be compared with approximately half of the elements in the sorted portion of 
the list before finding its correct position.
The number of comparisons and swaps is proportional to n^2, where n is the number of elements in the list.
In summary, the time complexity of Insertion Sort is O(n) in the best case, O(n^2) in the worst case, and O(n^2) in the average case. 
Despite its efficiency in the best case, Insertion Sort is generally less efficient than other sorting algorithms such as Merge Sort or Quick Sort for large lists due to its quadratic time complexity in the worst and average cases.
'''
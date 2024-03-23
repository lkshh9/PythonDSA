'''
Recursive Insertion SOrt

Base Case: if list has length 1 or 0, return the list
Inductive step:
    Inductively sort slice l[0:len(l)-1]
    Insert l[len(l)-1] into this sorted slice
'''

l = list(range(998,0,-1))

def InsertionSort(seq):
    isort(seq, len(seq))
    return seq

def isort(seq,k):  # Sort slice seq[0:k]
    if k>1:
        isort(seq,k-1)
        insert(seq,k-1)

def insert(seq,k): #Insert seq[k] into sorted seq[0:k-1]
    pos = k
    while pos>0 and seq[pos] < seq[pos-1]:
        (seq[pos], seq[pos-1]) = (seq[pos-1],seq[pos])
        pos = pos - 1

print(InsertionSort(l))


'''
def InsertionSort(seq):
    isort(seq, len(seq))
This line defines a function named InsertionSort that takes a sequence seq as its argument.
Inside the function, it calls another function isort(seq, len(seq)) to perform the Insertion Sort operation on the entire sequence.

def isort(seq, k):  # Sort slice seq[0:k]
    if k > 1:
        isort(seq, k - 1)
        insert(seq, k - 1)
This block defines a helper function named isort that performs the insertion sort recursively.
It takes two arguments: the sequence seq and the length k indicating the end index of the slice to be sorted.
Inside the function, it first checks if k is greater than 1. If it is, it continues with the sorting process. 
Otherwise, if k is 1 or less, it means the slice is already sorted or empty, so no further sorting is needed.
If k is greater than 1, it recursively calls isort(seq, k - 1) to sort the slice from index 0 to k-1.
After sorting the slice seq[0:k-1], it calls the insert function to insert the element at index k-1 into its correct position 
in the sorted slice.

def insert(seq, k):  # Insert seq[k] into sorted seq[0:k-1]
    pos = k
    while pos > 0 and seq[pos] < seq[pos - 1]:
        (seq[pos], seq[pos - 1]) = (seq[pos - 1], seq[pos])
        pos = pos - 1
This block defines another helper function named insert that inserts the element at index k into its correct position in 
the sorted slice seq[0:k-1].
It initializes a variable pos to k to track the position of the element being inserted.
It then enters a while loop that continues as long as pos is greater than 0 (to prevent indexing out of bounds) and the 
element at seq[pos] is less than the element before it seq[pos - 1].
Inside the loop, it swaps the current element with the element before it, effectively inserting the element into its correct position.
Finally, it decrements pos to continue iterating backwards through the sorted portion of the slice.
'''

# problem - maximum recursion depth
#   solution :
#     import sys
#     sys.setrecursionlimit(10000)
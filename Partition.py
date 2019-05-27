#------------------------------------------------
#Quicksort function
#------------------------------------------------


#When calling quicksort, you must input a list


"""
This program sorts a list from least to greatest by selecting a pivot and splitting the list into two partitions repeatealy until the whole list has been
been partitioned.
"""

"""
The user will call this function using quick_sort(array).
This function will call quicksort2 adding additional parameters, that being the 0 index and the highest index in the list
"""
def quick_sort(A):                                                                                                                                              #Declaration of function
    print ("quick")
    quick_sort2(A, 0, len(A)-1)
    return A

"""
quick_sort2 checks if the partition or list is greater than one and then declares p as the border from the partition (see partition) function
The function then runs quicksort2 two times again, one for the higher partition and the second time for the lower partition
"""
def quick_sort2 (A,low,hi):
    if low < hi:        #Add alternative sort (for efficency)
        p = partition (A, low, hi)
        quick_sort2(A, low, p - 1)
        quick_sort2(A, p + 1, hi)

"""
get_pivot selects a pivot based on the best of three method where you pick the first number in the partition, the last and the middle.
You then select the number which is the medium of the three and return the index value of the medium number
"""
def get_pivot(A, low, hi):
    mid = (hi + low) // 2
    pivot = hi
    if A[mid] > A[low] and A[mid] < A[hi]:
        pivot = mid
    elif A[mid] < A[low] and A[mid] > A[hi]:
        pivot = mid
    elif  A[low] < A[hi]:
        pivot = low
    return pivot 


"""
The partition function first finds the pivot (see get_pivot) and then declares pivotindex as the index number the pivot is in.
The pivotValue is the actual pivot number and the first number of the list withen the paramiters of the partitioned list is replaced with the pivot
The pivotindex is then placed as the the "border"
The program then checks every number in the partitioned part of the list and compares it to the pivotValue
If the number is less than the pivotValue, then the border is then moved up the list once and then swapped with the number that is less than the pivot value
This go on untill the the whole list has been checked.
Lastly the pivotindex (the first number in the partitioned list) is swaped with the border
This whole proccess will effectivily separate the list with all the large numbers on the right and small numbers on the left
The program will then return the border
"""
def partition (A, low, hi):
    pivotindex = get_pivot(A, low, hi)
    pivotValue = A[pivotindex]
    A[pivotindex], A[low] = A[low], A[pivotindex]
    border = low
    for x in range(low,hi+1):
        if A[x] < pivotValue:
            border = border + 1
            A[x], A[border] = A[border], A[x]
    A[low], A[border] = A[border], A[low]
    return (border)


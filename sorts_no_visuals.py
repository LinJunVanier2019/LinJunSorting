

#------------------------------------------------------------------------------
#------------------------------------------------
#Info on Quicksort
#------------------------------------------------
"""
Best Case: O (n log(n))
Worst Case: O (n**2)
Average Case: O (n log(n)) 
"""

#------------------------------------------------
#Quicksort function
#------------------------------------------------


"""
This program sorts a list from least to greatest by selecting a pivot and splitting the list into two partitions repeatealy until the whole list has been
been partitioned.
"""

"""
quick_sort checks if the partition or list is greater than one.

The partition function first finds the pivot (see get_pivot) and then declares pivotindex as the index number the pivot is in.
The pivotValue is the actual pivot number and the first number of the list withen the paramiters of the partitioned list is replaced with the pivot
The pivotindex is then placed as the the "border"
The program then checks every number in the partitioned part of the list and compares it to the pivotValue
If the number is less than the pivotValue, then the border is then moved up the list once and then swapped with the number that is less than the pivot value
This go on untill the the whole list has been checked.
Lastly the pivotindex (the first number in the partitioned list) is swaped with the border
This whole proccess will effectivily separate the list with all the large numbers on the right and small numbers on the left
then it will declares p as the border from the partition
The function then runs quicksort two times again, one for the higher partition and the second time for the lower partition
"""

def quick_sort (ilist,low,hi,no):
    
    if low < hi:
        
        pivotindex = get_pivot(ilist, low, hi)
        pivotValue = ilist[pivotindex]
        ilist[pivotindex], ilist[low] = ilist[low], ilist[pivotindex]
        border = low
        
        for x in range(low,hi+1):
            no += 1
            if ilist[x] < pivotValue:
                border = border + 1
                ilist[x], ilist[border] = ilist[border], ilist[x]
                
        ilist[low], ilist[border] = ilist[border], ilist[low]
        p = (border)
        quick_sort(ilist, low, p - 1,no)
        quick_sort(ilist, p + 1, hi,no)
    return no


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

#------------------------------------------------------------------------------
"""
Bubblesort sorts its list by comparing the first number with the next number, and the switch if the current number is larger then the
second. If the second number bigger, it will switch the numbers, else it will not switch. It will then check the next number and do the
same thing. This will sweep the entire list once and if there were no swaps, end the for loop pre-emptive, else keep going through for the
length of the list.
"""
def bubblesort(ilist):
    no = 0
    LOA = len(ilist)-1
    for i in range(LOA):
        hoop = 0
        for j in range(LOA - i):
            no += 1
            if ilist[j] > ilist[j+1]:
                
                ilist[j], ilist[j+1] = ilist[j+1], ilist[j]
            else:
                hoop +=1
        if hoop == len(ilist)-1:
            break
    return no
    
def insertionsort(ilist):
    no=0
    y = 1   #y-index starts at 1 instead of 0 - no numbers before index 0
    temp=0  
    while y < len(ilist):   # Loop will stop when y-index is equal to the length of the list
	    check = 0       # Reset exit condition

	    if ilist[y] <= ilist[y-1]:
	    	x = y
	    	while check !=1:
		    	if ilist[x] < ilist[x-1]:
			    	temp = ilist[x]
			    	ilist[x] = ilist[x-1]
			    	ilist[x-1] = temp
			    	no+=1
		    	else:
		    		check = 1
		    	x = x - 1
				
		    	if x == 0:
		    		check =  1
	    y = y + 1
    return no


#------------------------------------------------------------------------------
"""
Radix sort is similar to counting sort and bucket sort.
It creates buckets for each base digit (ie. 0-9)
And rearrange the list using counting sort.
It rearranges each number based on their radix
"""

def radixsort(ilist):
    no=0
    digit = 0        #set base digit
    maxdigit = 1     #to find biggest digit
    max_num = max(ilist)
    while max_num >= 10**maxdigit:
    	maxdigit += 1
			        
    while digit < maxdigit:
    	bucket = {}     #dictionary as 'bucket'
    	for x in range(10):        
    		bucket.setdefault (x,[])     #set each bucket from base 0-9
    	for num in ilist:
    		radix = int((num/(10**digit)%10))  #find its radix(number at the digit that's being checked)
    		bucket[radix].append(num)
    		no +=1
			
    	index=0
    	for check in range(10):
    		if len(bucket[check]) != 0:   #check if there is number in the bucket
    			for y in bucket[check]:
    				ilist[index] = y  #rearrange each number into the original list
					
    				index += 1        #in the order from the bucket
    	digit += 1   #loop stop when check digit reaches maxdigit
    return no
#------------------------------------------------------------------------------
"""
Merge sort is a devide-and-conquer algorithm.
It it based on the idea of repeatedly breaking the original list into half until each sublist only has one element.
Then merging all the sublists results a sorted list.
In merge sort, the concept of function recursion is used.
It is basically the idea of calling a function while defining it
To understand the concept, imagine two mirrors are placed face to face, therefore any object between wiil be reflected recursively
To better understand the use of function recursion here, imagine it as a tree diagram. It breaks down the orinal list.
into branches (left and right half), then keeps breaking the parent branches into more sub-branches.
When there is only one element left in each sublist. The following codes will sort each branch(sublist) from bottom to top.
"""
def mergesort (alist):
    no=mergesort2 (alist, 0)
    return no
def mergesort2(alist,no):
"""
This will keep dividing the left half of the original function until each sublist only has one element
"""
    if len(alist)>1:            
        mid =len(alist)//2       
        lefthalf =alist[:mid]   
        righthalf=alist[mid:]    

        mergesort2(lefthalf,no)      
    
        mergesort2(righthalf,no)   
        
        l=0                     
        r=0                      
        a=0                    
"""
Compare each index to another and merge them in the correct order
"""
        while l < len(lefthalf) and r < len(righthalf):
            no +=1
            if lefthalf[l] < righthalf[r]:                  
                alist[a] = lefthalf[l]                      
                l = l + 1                                   
                
            else :
                alist[a] = righthalf[r]
                r = r + 1
                no+=1
            a = a + 1                                       
            
        while l < len(lefthalf):        
            alist[a] = lefthalf[l]
            l = l + 1
            a = a + 1
            no += 1
            

        while r < len(righthalf):          
            alist[a] = righthalf[r]
            r = r + 1
            a = a + 1
            no+=1
    return no

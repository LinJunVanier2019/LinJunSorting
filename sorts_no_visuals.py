

#------------------------------------------------------------------------------


def quick_sort (ilist,low,hi):
    
    if low < hi:
        
        pivotindex = get_pivot(ilist, low, hi)
        pivotValue = ilist[pivotindex]
        ilist[pivotindex], ilist[low] = ilist[low], ilist[pivotindex]
        border = low
        
        for x in range(low,hi+1):
            if ilist[x] < pivotValue:
                border = border + 1
                ilist[x], ilist[border] = ilist[border], ilist[x]
                
        ilist[low], ilist[border] = ilist[border], ilist[low]
        p = (border)
        quick_sort(ilist, low, p - 1)
        quick_sort(ilist, p + 1, hi)
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

def bubblesort(ilist):
    hi = len(ilist)-1
    check = True
    while check == True:
        checks = False
        for x in range (0,hi):
            if ilist[x] > ilist[x+1]:
                temp = ilist[x]
                ilist[x] = ilist[x+1]
                ilist[x+1] = temp
                check = True
                checks = True
            else:
                if checks != True:
                    check = False
        hi -= 1
    
def insertionsort(ilist):
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
		    	else:
		    		check = 1
		    	x = x - 1
				
		    	if x == 0:
		    		check =  1
	    y = y + 1


#------------------------------------------------------------------------------


def radixsort(ilist):
    digit = 0        #set base digit
    maxdigit = 1     #to find biggest digit
    max_num = max(ilist)
    while max_num > 10**maxdigit:
    	maxdigit += 1
			        
    while digit < maxdigit:
    	bucket = {}     #dictionary as 'bucket'
    	for x in range(10):        
    		bucket.setdefault (x,[])     #set each bucket from base 0-9
    	for num in ilist:
    		radix = int((num/(10**digit)%10))  #find its radix(number at the digit that's being checked)
    		bucket[radix].append(num)  #arrange each number in to its bucket
			
    	index=0
    	for check in range(10):
    		if len(bucket[check]) != 0:   #check if there is number in the bucket
    			for y in bucket[check]:
    				ilist[index] = y  #rearrange each number into the original list
					
    				index += 1        #in the order from the bucket
    	digit += 1   #loop stop when check digit reaches maxdigit



#------------------------------------------------------------------------------


def mergesort(alist):
    if len(alist)>1:            
        mid =len(alist)//2       
        lefthalf =alist[:mid]   
        righthalf=alist[mid:]    

        mergesort(lefthalf)      
    
        mergesort(righthalf)   
        
        l=0                     
        r=0                      
        a=0                    

        while l < len(lefthalf) and r < len(righthalf):     
            if lefthalf[l] < righthalf[r]:                  
                alist[a] = lefthalf[l]                      
                l = l + 1                                   

            else :
                alist[a] = righthalf[r]
                r = r + 1
            a = a + 1                                       
            
        while l < len(lefthalf):        
            alist[a] = lefthalf[l]
            l = l + 1
            a = a + 1


        while r < len(righthalf):          
            alist[a] = righthalf[r]
            r = r + 1
            a = a + 1

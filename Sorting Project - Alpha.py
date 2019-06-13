import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import random

#--------------------------------------------------------------------------------
#Quick Sort
def quick_sort(ilist):
        yield from quick_sort2(ilist,0,len(ilist)-1)
def quick_sort2 (ilist,low,hi):
    if low < hi:
        
        pivotindex = get_pivot(ilist, low, hi)
        pivotValue = ilist[pivotindex]
        ilist[pivotindex], ilist[low] = ilist[low], ilist[pivotindex]
        border = low
        
        for x in range(low,hi+1):
            if ilist[x] < pivotValue:
                border = border + 1
                ilist[x], ilist[border] = ilist[border], ilist[x]
                yield ilist
        ilist[low], ilist[border] = ilist[border], ilist[low]
        p = (border)
        yield ilist
        yield from quick_sort2(ilist, low, p - 1)
        yield from quick_sort2(ilist, p + 1, hi)
        

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
#-------------------------------------------------------------------------------
#Bubble Sort
def bubble_sort (ilist):
    hi = len(ilist)-1
    check = True
    while check == True:
        checks = False
        for x in range (0,hi):
            if ilist[x] > ilist[x+1]:
                temp = ilist[x]
                ilist[x] = ilist[x+1]
                ilist[x+1] = temp
                yield ilist
                check = True
                checks = True
            else:
                if checks != True:
                    check = False
        hi -= 1           
    yield ilist
#-------------------------------------------------------------------------------
#Insertion Sort
def insertion_sort (ilist):
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
					yield ilist
					rect.set_color('green')
				else:
					check = 1
				x = x - 1
				
				if x == 0:
					check =  1
			yield ilist
		y = y + 1
#-------------------------------------------------------------------------------
#Radix Sort
def radix_sort(ilist):
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
					yield ilist
					index += 1        #in the order from the bucket
		digit += 1   #loop stop when check digit reaches maxdigit
#------------------------------------------------------------------------------
#Merge Sort
def merge_sort(ilist):
        yield from mergesort(ilist,0,len(ilist)-1)
def mergesort(ilist, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from mergesort(ilist, start, mid)
    yield from mergesort(ilist, mid + 1, end)
    yield from merge(ilist, start, mid, end)
    yield ilist

def merge(ilist, start, mid, end):
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if ilist[leftIdx] < ilist[rightIdx]:
            merged.append(ilist[leftIdx])
            leftIdx += 1
        else:
            merged.append(ilist[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(ilist[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(ilist[rightIdx])
        rightIdx += 1

    for i, sorted_num in enumerate(merged):
        ilist[start + i] = sorted_num
        yield ilist
#------------------------------------------------------------------------------		
rect = None
ilist = []
for x in range (0,25):
        ilist.append(random.randint(0,500))
max_num = max(ilist)
N=0
for length in ilist:
        N = N + 1
if __name__ == "__main__":
        print ("Sort Menu:")
        print ("1. Quick Sort")
        print ("2. Bubble Sort")
        print ("3. Insertion Sort")
        print ("4. Radix Sort")
        print ("5. Merge Sort")
        
        sort_list = [quick_sort, bubble_sort, insertion_sort, radix_sort, merge_sort]
        
        sort_type = int(input("Please enter number representing sort type."))

        generator = sort_list[sort_type-1](ilist)

        title = ["Quick Sort","Bubble Sort","Insertion Sort","Radix Sort","Merge Sort"]
        
        fig, ax = plt.subplots()
        ax.set_title(title[sort_type-1])
                        
        bar_rects = ax.bar(range(len(ilist)), ilist, align="edge")
        ax.set_xlim(0, N)
        ax.set_ylim(0, int(max_num*1.2))
        text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
        iteration = [0]
        def update_fig(ilist, rects, iteration):
                global rect 
                for rect, val in zip(rects, ilist): #zip joins rect and ilist coordiantes in pairs
                        rect.set_height(val)
                iteration[0] += 1
                        
                text.set_text("# of operations: {}".format(iteration[0]))

                                           
        anim = animation.FuncAnimation(fig, func=update_fig,
            fargs=(bar_rects, iteration), frames=generator, interval=1,
            repeat=False)
        plt.show()

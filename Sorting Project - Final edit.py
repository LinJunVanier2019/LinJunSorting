import tkinter as tk
import csv
from memory_profiler import profile


#------------------------------------
"""
Reading text file for list
"""


#@profile(precisiom=4)
global ilist2
ilist2 = []
temp_lis = []
with open ("yagmai.txt") as tf:
    rtf = csv.reader(tf, delimiter = ",")
    for line in rtf:
        for p in range (len(line)):
            temp_lis.append(int(line[p]))
        ilist2.extend(temp_lis)
        temp_lis = []

#-------------------------------------
#No Visuals
def quick():
    ilist = ilist2
    quick_sort(ilist,0,len(ilist)-1)
    print(ilist)
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

def bubble():
    ilist = ilist2
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
    print(ilist)
    
def insertion():
    ilist = ilist2
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
    print(ilist)
def radix():
    ilist = ilist2
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
    print (ilist)
def merge(ilist,start,mid,end):
    ilist = ilist2
    mergesort(ilist,0,len(ilist)-1)
    print (ilist)
def mergesort(ilist, start, end):
    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    mergesort(ilist, start, mid)
    mergesort(ilist, mid + 1, end)
    merge(ilist, start, mid, end)

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
#-------------------------------------

def visuals():
    print("visuals graphs")

def no_visuals():
    main2()

def main2():
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
    button.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                   text="Quick Sort",
                   command=quick )
    slogan.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                   text="Bubble Sort",
                   command=bubble )
    slogan.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                   text="Insertion Sort",
                   command=insertion )
    slogan.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                   text="Radix Sort",
                   command=radix )
    slogan.pack(side=tk.LEFT)
    slogan = tk.Button(frame,
                   text="Merge Sort",
                   command=merge )
    slogan.pack(side=tk.LEFT)
def main():
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
    button.pack(side=tk.LEFT)

    slogan = tk.Button(frame,
                   text="Visuals",
                   command=visuals )
    slogan.pack(side=tk.LEFT)


    Oof = tk.Button(frame,
                   text="No Visuals",
                   command=no_visuals)
    Oof.pack(side=tk.LEFT)


    root.minsize(500,500)
    root.maxsize(500,500)
    root.mainloop()
#----------------------------------------------
if ilist2 == []:
    print ("please enter list into yagmai.txt text file")
    print ("with a format like ##,##,##,##")
else:
    print ("Your list is :", ilist2)
    main()

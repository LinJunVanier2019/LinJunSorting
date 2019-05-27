import os
import os.path
import time
from Partition import quick_sort  #quick_sort(A)     
from BubbleSort import bubblesort   #bubblesort(A)
from Radix import radixSort     #radixSort(A)
from Merge import mergesort     #mergesort(A)
lis = []

import random
for x in range (1,1000):
    lis.append (random.randint(1,10000))
    


"""
User Prompt function to get the sort he wants and the calls the error trap function
"""
def cSort2(SL,A):
    print ("What sort do you want to use")
    C = int(input("Enter a number from 1 to 4: "))     #CHANGE NUMBER TO AMOUNT OF SORT FUNCTIONS
    cCheck(SL,C-1,A)    

def cCheck(SL,C,A):
    try:
        A = SL[C](A)
    except IndexError:
        print (" ")
        print ("Sort is not in range")
        print (" ")
        cSort2(SL,A)
        
def cSort(A):
    sort_list = [quick_sort, bubblesort, radixSort, mergesort]    #ADD SORT FUNCTIONS TO HERE
    start = time.time()     #This takes the time the function starts 
    cSort2(sort_list,A)
    end = time.time ()      #this takes the time the function program ends
    print ("Time :", end - start)    #This calculates the time it took for the program to run
    return A

print (cSort(lis))

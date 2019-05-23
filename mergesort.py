"""
Hello this library defines the function of merge sort
"""


"""
    Merge sort is a devide-and-conquer algorithm.
    It it based on the idea of repeatedly breaking the original list into half until each sublist only has one element.
    Then merging all the sublists results a sorted list.
"""


"""
    The following codes are used to break the parent list into half.
    The if statement is to check if the sublist only has one element.
"""
   
"""
    In merge sort, the concept of function recursion is used.
    It is basically the idea of calling a function while defining it
    To understand the concept, imagine two mirrors are placed face to face, therefore any object between wiil be reflected recursively
"""


"""
    The reason why function recursion is used is because merge sort requires to break the list into multiple sublists until
    each sublist only has one element, and then merge them.
"""


"""
    To better understand the use of function recursion here, imagine it as a tree diagram. It breaks down the orinal list.
    into branches (left and right half), then keeps breaking the parent branches into more sub-branches.
    When there is only one element left in each sublist. The following codes will sort each branch(sublist) from bottom to top.
"""
"""
        This will keep dividing the left half of the original function until each sublist only has one element
"""
def mergesort(alist):
    if len(alist)>1:             #check if there is only 1 element
        mid =len(alist)//2       #find mid of list
        lefthalf =alist[:mid]    #get left half
        righthalf=alist[mid:]    #get right half
#----------------function recursion-------------
        mergesort(lefthalf)      #function recursion,keep diving into sublists until there is only one element
        """
        This will divide the right half of each parent lists        
        """
        mergesort(righthalf)     #function recursion,keep diving into sublists until there is only one element

        
        l=0                      #left half index number
        r=0                      #right half index number
        a=0                      #parent list index number

        """
        Compare each index to another and merge them in the correct order
        """
        while l < len(lefthalf) and r < len(righthalf):     #compare repeatly until list is sorted
            if lefthalf[l] < righthalf[r]:                  #compare 2 sublists from the same parent list
                alist[a] = lefthalf[l]                      #sorting parent list
                l = l + 1                                   #make sure while loop condition will be met

            else :
                alist[a] = righthalf[r]
                r = r + 1
            a = a + 1                                       #increasing index of parent list,make sure each sorted element goes into the right place
            
#---------------after process above, there would be 1 element left. Either from lefthalf or righthalf------------------------
        """
        Sorting the left sides of each parent function
        """
        while l < len(lefthalf):           #1 element left from left
            alist[a] = lefthalf[l]
            l = l + 1
            a = a + 1
        """
        sorting the right sides of each parent function
        """

        while r < len(righthalf):          #1 element left from right
            alist[a] = righthalf[r]
            r = r + 1
            a = a + 1
#---------------after process above, the parent list is sorted-------------------

    
import time
import random
alist = []
for i in range(0,1000):
        num= random.randint(1,99999999)
        alist.append(num)
start = time.time()
mergesort(alist)
end = time.time()
print (end-start)


        

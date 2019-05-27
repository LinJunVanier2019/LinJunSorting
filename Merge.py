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

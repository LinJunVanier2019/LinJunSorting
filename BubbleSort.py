#------------------------------------------------
#Bubblesort function
#------------------------------------------------


def bubblesort (A):
    print ("bubble")
    hi = len(A)-1
    check = True
    while check == True:
        checks = False
        for x in range (0,hi):
            if A[x] > A[x+1]:
                temp = A[x]
                A[x] = A[x+1]
                A[x+1] = temp
                check = True
                checks = True
                
            else:
                if checks != True:
                    check = False
        hi -= 1           
    return (A)



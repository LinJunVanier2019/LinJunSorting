def insertion_sort (ilist):
    y = 1
    temp=0
    while y < len(ilist):
	check = 0
	if ilist[y] <= ilist[y-1]:
	    x = y
	    while check !=1 and x != 0:
		if ilist[x] < ilist[x-1]:
		    temp = ilist[x]
		    ilist[x] = ilist[x-1]
		    ilist[x-1] = temp
		else:
		    check = 1
		x = x - 1
	    y = y+1

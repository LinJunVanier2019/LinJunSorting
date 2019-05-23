
#   Algorithm : Radix Sort


"""
    Time Complexity :

        Best-case : O(kn); Average-case : O(kn); Worst-case : O(kn)
        Where k is the length of the largest number in the list
        and n is the size of the list

    Space Complexity:

        O(k+n)
"""

"""
        Radix sort is similar to counting sort and bucket sort.
        It creates buckets for each base digit (ie. 0-9)
        And rearrange the list using counting sort.
        It rearranges each number based on their radix
        
"""



def radixSort(alist):
	digit = 0        #set base digit
	maxdigit = 1     #to find biggest digit
	max_num = max(alist)
	while max_num > 10**maxdigit:
		maxdigit += 1
		
		        
	while digit < maxdigit:
		bucket = {}     #dictionary as 'bucket'
		for x in range(10):        
			bucket.setdefault (x,[])     #set each bucket from base 0-9
		for num in alist:
			radix = int((num/(10**digit)%10))  #find its radix(number at the digit that's being checked)
			bucket[radix].append(num)  #arrange each number in to its bucket

			
		index=0
		for check in range(10):
			if len(bucket[check]) != 0:   #check if there is number in the bucket
				for y in bucket[check]:
					alist[index] = y  #rearrange each number into the original list
					index += 1        #in the order from the bucket
		digit += 1   #loop stop when check digit reaches maxdigit







import time
import random
alist = []
for i in range(0,100000):
        num= random.randint(1,99999999)
        alist.append(num)
start = time.time()
radixSort(alist)
end = time.time()
print (end-start)

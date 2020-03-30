#Adding of Elements

import time
t0=time.time()
def Sum(A):
	s=0
	for  i in range(len(A)):
		s+=A[i]
	print(s)

A=[1,2,3,4,5,6,7,8,9]
Sum(A)
t1=time.time()
print("Runtime : ",t1-t0)


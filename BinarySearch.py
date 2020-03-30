def BinaryS(A,key):
	s=0
	l=len(A)-1
	while s<=l:
		mid=int((s+l)//2)
		if A[mid]==key:
			return mid
		elif A[mid]>key:
			l=mid-1
		else:
			s=mid+1
	return -1

A=[1,2,4,7,12,26,85,92,150,190,345]
key = 345

print(BinaryS(A,key))
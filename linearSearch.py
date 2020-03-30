def linear(A,key):
	for i in range(len(A)):
		if A[i]==key:
			return i
	return -1

A=[1,2,3,4,5,6,7,8,9]
key=5
print(linear(A,key))
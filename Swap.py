# Program for swapping of two elements
import timeit

t0=timeit.default_timer()
a=2
b=3
a,b=b,a
print(a,b)
t1=timeit.default_timer()
print("Runtime : ",t1-t0)

#Swapping of elements using function

s=timeit.default_timer()
def swap(a,b):
	t=a
	a=b
	b=t
	return a,b

print(swap(2,3))
e=timeit.default_timer()
print("Runtime : ",e-s)

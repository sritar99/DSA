from exceptions import Empty
class ArrayStack:
	def __init__(self):
		self._data=[]
	def _len(self):
		return len(self._data)
	def _isEmpty(self):
		return len(self._data)==0
	def _push(self,ele):
		self._data.append(ele)
	def _pop(self):
		if self._isEmpty():
			raise Empty("Stack is Empty")
		else:
			return self._data.pop()
	def top(self,ele):
		if self._isEmpty():
			raise Empty("Stack is Empty")
		else:
			return self._data[-1]


Stack =ArrayStack()
print(Stack._len())
print(Stack._push(5))
print(Stack._push(10))
print(Stack._push(15))
print(Stack._data)
print(Stack._pop())
print(Stack._data)
print(Stack._push(20))
print(Stack._data)
print(Stack._pop())
print(Stack._data)
print(Stack._len())
print(Stack._data)



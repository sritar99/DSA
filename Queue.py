from exceptions import Empty
class QueArr:
	def __init__(self):
		self._data=[]
		self.size=0
		self.front=0
	def _len(self):
		return len(self._data)
	def isEmpty(self):
		return len(self._data)==0
	def enque(self,ele):
		self._data.append(ele)
		self.size+=1
	def deque(self):
		if self.isEmpty():
			raise Empty("Que is Empty")
		else:
			val=self._data[self.front]
			self._data[self.front]=None
			self.front+=1
			self.size-=1
			return val
	def first(self):
		if self.isEmpty():
			raise Empty("Que is Empty")
		else:
			return self._data[self.front]


q=QueArr()
q.enque(3)
q.enque(5)
q.enque(31)
q.enque(54)
q.enque(32)
q.enque(57)
print(q._data)
print(q.deque())
print(q.deque())
print(q._data)
print(q.first())
print(q.deque())
print(q.deque())
print(q._data)
print(q.first())
print(q._len())
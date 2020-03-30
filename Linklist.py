from exceptions import Empty
class LinkList:
	class _Node:
		def __init__(self,ele):
			self._data=ele
			self.next=None

	def __init__(self):
		self.head=None
		self.tail=None
		self.size=0
	def _len(self):
		return self.size

	def _isEmpty(self):
		return self.size==0

	def addF(self,ele):
		new=self._Node(ele)
		if self.head==None:
			self.head=new
			self.tail=new
		else:
			new.next= self.head
		self.head=new
		self.size+=1

	def addL(self,ele):
		new=self._Node(ele)
		if self.head==None:
			self.head=new
			self.tail=new
		else:
			self.tail.next=new
		self.tail=new
		self.size+=1
	def addAny(self,ele,pos):
		i=1
		new=self._Node(ele)
		tmp = self.head
		while i<pos:
			tmp = tmp.next 
			i+=1
		new.next=tmp.next
		tmp.next=new
		self.size+=1

	def removeF(self):
		if self._isEmpty():
			raise Empty("list is empty")
		val=self.head.ele
		self.size-=1
		self.head=self.head.next
		if self._isEmpty():
			self.tail=None
		return val

	def removeL(self):
		if self._isEmpty():
			raise Empty("list is empty")
		tmp=self.head
		i=0
		while i<len(self)-2:
			tmp = tmp.next
			i+=1

		self.tail=tmp
		tmp=tmp.next
		val=tmp._data
		self.tail.next=None
		self.size-=1
		return val
	def removeAny(self,pos):
		if self._isEmpty():
			raise Empty("list is empty")
		tmp=self.head
		i=1
		while i<pos-1:
			tmp = tmp.next
			i+=1
		val =tmp.next._data
		tmp.next=tmp.next.next
		self.size-=1
		return val
	def display(self):
		tmp=self.head
		while tmp:
			print(tmp._data,end="-->")
			tmp=tmp.next
		print()

LL=LinkList()
LL.addF(10)
LL.addF(5)
LL.addL(20)
LL.addAny(15,2)
LL.display()





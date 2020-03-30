class LinkList:

	class Node:
		def __init__(self,ele):
			self.data=ele
			self.next=None

	def __init__(self):
		self.head=None
		self.size=0

	def isEmpty(self):
		return self.size==0

	def getLen(self):
		return self.size

	def addatHead(self,ele):
		new=Node(ele)
		if isEmpty():
			self.head=new

		else:
			new.next=self.head
			self.head=new

		self.size+=1

	def addatLast(self,ele):
		new=Node(ele):
		t=self.head
		while t.next!=None:
			t=t.next
		t.next=new
		self.size+=1

	def addatPos(self,index,ele):
		if isEmpty():
			print("LinkList is empty! can't add element at required position")
			return 0
		new=Node(ele)
		pos=1
		t=self.head
		while pos<index:
			t=t.next
			pos+=1
		new.next=t.next
		t.next=new
		self.size+=1

	def removeF(self):
		if isEmpty():
			print("LinkList is empty! can't remove element at required position")
			return 0
		t=self.head
		print(t.data)
		t.next=None
		self.head=self.head.next
		del(t)
		self.size-=1
	
	def removeL(self):
		if isEmpty():
			print("LinkList is empty! can't remove element at required position")
			return 0
		t=self.head
		while t.next.next!=None:
			t=t.next
		val=t.next.data
		print(val)
		t.next=None
		self.size-=1

	def removePos(self,index):
		if isEmpty():
			print("LinkList is empty! can't remove element at required position")
			return 0
		t=self.head
		i=1
		while i<index:
			t=t.next
			i+=1
		val=t.next.data
		print(val)
		t.next=t.next.next
		self.size-=1

	def display(self):
		tmp=self.head
		while tmp:
			print(tmp._data,end="-->")
			tmp=tmp.next
		print()

LL=LinkList()
LL.addatHead(10)
LL.addatHead(5)
LL.addatLast(20)
LL.addatPos(2,15)
LL.display()





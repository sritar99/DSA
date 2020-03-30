class BST:
	class Node:
		def __init__(self,val):
			self.data=val
			self.left=None
			self.right=None


	def Search(root,val):
		if root is None or root.data == val :
			return root

		if root.data<val:
			return Search(root.right,val)

		return Search(root.left,val)


	def insert(root,node):
		if root is None:
			root=node
		else:
			if root.data<node.data:
				if root.right is None:
					root.right=node
				else:
					insert(root.right,node)

			else:
				if root.left is None:
					root.left=node
				else:
					insert(root.left,node)


	def deleteNode(root, key): 
  
    # Base Case 
    	if root is None: 
        	return root  
  
    # If the key to be deleted is smaller than the root's 
    # key then it lies in  left subtree 
    	if key < root.key: 
        	root.left = deleteNode(root.left, key) 
  
    # If the kye to be delete is greater than the root's key 
    # then it lies in right subtree 
    	elif(key > root.key): 
        	root.right = deleteNode(root.right, key) 
  
    # If key is same as root's key, then this is the node 
    # to be deleted 
    	else: 
          
        # Node with only one child or no child 
        	if root.left is None : 
            	temp = root.right  
            	root = None 
            	return temp  
              
        	elif root.right is None : 
            	temp = root.left  
            	root = None
            	return temp 
  
        # Node with two children: Get the inorder successor 
        # (smallest in the right subtree) 
        	temp = minValueNode(root.right) 
  
        # Copy the inorder successor's content to this node 
        	root.key = temp.key 
  
        # Delete the inorder successor 
        	root.right = deleteNode(root.right , temp.key) 
  
  
    	return root

	def minValueNode( node): 
    		current = node 
  
    		# loop down to find the leftmost leaf 
    		while(current.left is not None): 
        		current = current.left  
  
    		return current

	def getLevelOrder(root):
		h=height(root)
		for i in range(1,h+1):
			printLevel(root,i)


	def printLevel(root,level):
		if root is None:
			return
		if level==1:
			print(root.data)
		elif level>1:
			printLevel(root.left,level-1)
			printLevel(root.right,level-1)


	def height(root):
		if root is None:
			return 0
		else:
			left = height(root.left)
			right = height(root.right)
			return max(left,right)+1

	def inorder(root):
		if root:
			inorder(root.left)
			print(root.val)
			inorder(root.right)

	def preorder(root):
		if root:
			print(root.val)
			preorder(root.left)
			preorder(root.right)

	def postorder(root):
		if root:
			postorder(root.left)
			postorder(root.right)
			print(root.val)		



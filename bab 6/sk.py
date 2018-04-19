import os
class Node(object):
    def __init__(self, data):
        self.data = data
        self.l = None
        self.r = None

    def insert(self, data):
        if self.data == data:
            return False

        elif data < self.data:
            if self.l:
                return self.l.insert(data)
            else:
                self.l = Node(data)
                return True

        else:
            if self.r:
                return self.r.insert(data)
            else:
                self.r = Node(data)
                return True

    def minValueNode(self, node):
        current = node

        while(current.l is not None):
            current = current.l

        return current

    def delete(self, data):
        if self is None:
            return None

        if data < self.data:
            self.l = self.l.delete(data)
        elif data > self.data:
            self.r = self.r.delete(data)
        else:
            if self.l is None:
                temp = self.r
                self = None
                return temp
            elif self.r is None:
                temp = self.l
                self = None
                return temp

            temp = self.minValueNode(self.r)
            self.data = temp.data
            self.r = self.r.delete(temp.data)

        return self

    def search(self, data):
        if(data == self.data):
            return True
        elif(data < self.data):
            if self.l:
                return self.l.search(data)
            else:
                return False
        else:
            if self.r:
                return self.r.search(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.data))
            if self.l:
                self.l.preorder()
            if self.r:
                self.r.preorder()

    def inorder(self):
        if self:
            if self.l:
                self.l.inorder()
            print(str(self.data))
            if self.r:
                self.r.inorder()

    def postorder(self):
        if self:
            if self.l:
                self.l.postorder()
            if self.r:
                self.r.postorder()
            print(str(self.data))

class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data)

    def search(self, data):
        if self.root:
            return self.root.search(data)
        else:
            return False

    def preorder(self):
        if self.root is not None:
            print('Preorder: ')
            self.root.preorder()

    def inorder(self):
        if self.root is not None:
            print('Inorder: ')
            self.root.inorder()

    def postorder(self):
        if self.root is not None:
            print('Postorder: ')
            self.root.postorder()

if __name__ == '__main__':
	t = Tree()
	while True:
		os.system('pause')
		print 'TTTTTTT  RRRRR   EEEEE  EEEEE\n' \
		      '   T     R    R  E      E\n' \
		      '   T     RRRRR   EEEEE  EEEEE\n' \
		      '   T     R   R   E      E\n' \
		      '   T     R    R  EEEEE  EEEEE\n' \
		      '\n' \
		      '1. Insert Data\n' \
		      '2. Search Data\n' \
		      '3. Delete Data\n' \
		      '4. Show Pre-Order\n' \
		      '5. Show In-Order\n' \
		      '6. Post-Order'
		x = str(raw_input('Choose from Menu : '))
		if x=='1':
			obj = raw_input('Input Data to Tree : ')
			t.insert(obj)
			print obj, ' Inserted'
		elif x=='2':
			obj = raw_input('Input Data to Search : ')
			t.search(obj)
		elif x=='3':
			obj = raw_input('Input Data to Delete : ')
			t.delete(obj)
		elif x=='4':
			t.preorder()
		elif x=='5':
			t.inorder()
		elif x=='6':
			t.postorder()
		else:
			print 'Wrong Menu'
			break

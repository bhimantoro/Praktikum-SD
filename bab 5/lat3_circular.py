class Node(object):

	def __init__(self, d, n = None):
		self.data = d
		self.next_node = n

	def get_next(self):
		return self.next_node

	def set_next(self, n):
		self.next_node = n
		
	def get_data(self):
		return self.data

	def set_data(self, d):
		self.data = d
		
	def to_string(self):
		return "Node value: " + str(self.data)

class CircularLinkedList(object):

	def __init__(self, r = None):
		self.root = r
		self.size = 0

	def get_size(self):
		return self.size

	def add(self, d):
		if self.get_size() == 0:
			self.root = Node(d)
			self.root.set_next(self.root)
		else:
			new_node = Node(d, self.root.get_next())
			self.root.set_next(new_node)
		self.size += 1

	def remove(self, d):
		this_node = self.root
		prev_node = None

		while True:
			if this_node.get_data() == d:# found
				if prev_node is not None:
					prev_node.set_next(this_node.get_next())
				else:
					while this_node.get_next() != self.root:
						this_node = this_node.get_next()
					this_node.set_next(self.root.get_next())
					self.root = self.root.get_next()
				self.size -= 1
				return True     # data removed
			elif this_node.get_next() == self.root:
				return False	# data not found
			prev_node = this_node
			this_node = this_node.get_next()

	def find(self, d):
		this_node = self.root
		while True:
			if this_node.get_data() == d:
				print("founded")
				return d
			elif this_node.get_next() == self.root:
				print("not found")
				return False
			this_node = this_node.get_next()
		
	def print_list(self):
		print("Print List..........")
		if self.root is None:
			return
		this_node = self.root
		print(this_node.to_string())
		while this_node.get_next() != self.root:
			this_node = this_node.get_next()
			print(this_node.to_string())

	def mainmenu(self):
		while True:
			print "Circular Linked List\n" \
			  "1.\tInsert Data\n"\
			  "2.\tRemove Data\n"\
			  "3.\tFind Data\n"\
			  "4.\tShow Data\n"
			pil = str(raw_input("Choose Menu : "))
			if pil == '1':
				obj = str(raw_input("Input Data : "))
				self.add(obj)
			elif pil == '2':
				obj = str(raw_input("Remove Data : "))
				self.remove(obj)
			elif pil == '3':
				obj = str(raw_input("Find Data : "))
				self.find(obj)
			elif pil == '4':
				print("Circular Linked List")
				self.print_list()
			else:
				break

if __name__ == '__main__':
	cll = CircularLinkedList()
	cll.mainmenu()

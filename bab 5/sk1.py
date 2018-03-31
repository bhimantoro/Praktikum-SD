import os
class Node(object):
	def __init__(self, data=None, nextNode=None):
		self.data = data
		self.nextNode = nextNode

	def getData(self):
		return self.data

	def getNext(self):
		return self.nextNode

	def setNext(self, newNext):
		self.nextNode = newNext

class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def push(self, data):
		newNode = Node(data)
		newNode.setNext(self.head)
		self.head = newNode

	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.getNext()
		return count
	def search(self, data):
		current = self.head
		found = False
		while current and found is False:
			if current.getData() == data:
				found = True
			else:
				current = current.getNext()
		return found

	def delete(self, data):
		current = self.head
		previous = None
		found = False
		while current and found is False:
			if current.getData() == data:
				found = True
			else:
				previous = current
				current = current.getNext()
		if current is None:
			raise ValueError("Data not in list")
		if previous is None:
			self.head = current.getNext()
		else:
			previous.set_next(current.getNext())

	def showData(self):
		os.system('cls')
		print ("Tampilkan list data:")
		print ("Node -> Next Node")
		current_node = self.head
		while current_node is not None:
			print (current_node.data),(" ->"),(current_node.nextNode.data) if hasattr(current_node.nextNode, "data") else None

			current_node = current_node.nextNode

	def menu(self):
		while True:
			#menu
			pil = raw_input("Choose Menu : ")
			if pil == '1':
				obj = str(raw_input("Input Data : "))
				self.push(obj)
			elif pil == '2':
				obj = str(raw_input("Delete Data : "))
				self.delete(obj)
			elif pil == '3':
				self.showData()
			else:
				break

if __name__ == '__main__':
	l = LinkedList()
	l.menu()

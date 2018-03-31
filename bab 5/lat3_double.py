class Node(object):
	def __init__(self, data, next = None, previous = None):
		self.data = data;
		self.next = next;
		self.previous = previous

class DoublyLinkedList(object):
	def __init__(self):
		self.head = None

	def insertAtStart(self, data):
		if self.head == None:
			newNode = Node(data)
			self.head = newNode
		else:
			newNode = Node(data)
			self.head.previous = newNode
			newNode.next = self.head
			self.head = newNode

	def insertAtEnd(self, data):
		newNode = Node(data)
		temp = self.head
		while(temp.next != None):
			temp = temp.next
		temp.next = newNode
		newNode.previous = temp

	def delete(self, data):
		temp = self.head
		if(temp.next != None):
			if(temp.data == data):
				temp.next.previous = None
				self.head = temp.next
				temp.next = None
				return
			else:
				while(temp.next != None):
					if(temp.data == data):
						break
					temp = temp.next
				if(temp.next):
					temp.previous.next = temp.next
					temp.next.previous = temp.previous
					temp.next = None
					temp.previous = None
				else:
					temp.previous.next = None
					temp.previous = None
				return

		if (temp == None):
			return

	def printdll(self):
		temp = self.head
		while(temp != None):
			print temp.data
			temp = temp.next

	def mainmenu(self):
		while True:
			print "Double Linked List\n" \
			  "1.\tInsert Data At The Beginning\n"\
			  "2.\tInsert Data At The End\n"\
			  "3.\tDelete Data\n"\
			  "4.\tTampil Data\n"
			pil = str(raw_input("Choose Menu : "))
			if pil == '1':
				obj = str(raw_input("Input : "))
				self.insertAtStart(obj)
			elif pil == '2':
				obj = str(raw_input("Input : "))
				self.insertAtEnd(obj)
			elif pil == '3':
				obj = str(raw_input("Delete Data : "))
				self.delete(obj)
			elif pil == '4':
				print("DoublyLinkedList")
				self.printdll()
			else:
				break
if __name__ == '__main__':
	dll = DoublyLinkedList()
	dll.mainmenu()

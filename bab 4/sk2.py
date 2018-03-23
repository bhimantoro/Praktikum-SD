'''
#Menggunakan Linked list
class StackNode:
	# Constructor to initialize a node
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:
	# Constructor to initialize the root of linked list
	def __init__(self):
		self.root = None

	def isEmpty(self):
		return True if self.root is None else  False

	def push(self, data):
		newNode = StackNode(data)
		newNode.next = self.root
		self.root = newNode
		print data + " pushed to stack"

	def pop(self):
		if (self.isEmpty()):
			return float("-inf")
		temp = self.root
		self.root = self.root.next
		popped = temp.data
		return popped

	def peek(self):
		if self.isEmpty():
			return float("-inf")
		return self.root.data

def main():
	s = Stack()
	while True:
		print '1.\tPush\n' \
			  '2.\tPop\n' \
			  '3.\tPrint'
		x = int(raw_input("Choose Menu : "))

		if x == 1:
			s.push(str(raw_input("Input Stack : ")))
		elif x == 2:
			print "popped from stack" + s.pop()
		elif x == 3:
			print s
		else:
			break

main()
'''
class Stack(object):
	def __init__(self, limit = 10):
		self.stack = []
		self.limit = limit

	# for printing the stack contents
	def __str__(self):
		return ' '.join([str(i) for i in self.stack])

	# for pushing an element on to the stack
	def push(self, data):
		if len(self.stack) >= self.limit:
			print('Stack Overflow')
		else:
			self.stack.append(data)
			print data + " pushed to stack "

	# for popping the uppermost element
	def pop(self):
		if len(self.stack) <= 0:
			return -1
		else:
			return self.stack.pop()

	# for peeking the top-most element of the stack
	def peek(self):
		if len(self.stack) <= 0:
			return -1
		else:
			return self.stack[len(self.stack) - 1]

	# to check if stack is empty
	def isEmpty(self):
		return self.stack == []

	# for checking the size of stack
	def size(self):
		return len(self.stack)

def main():
	s = Stack()
	while True:
		print '\n\nStack Implementaion\n'\
		      '1.\tPush Element\n' \
			  '2.\tPop Element\n' \
			  '3.\tPrint Stack Element\n' \
		      '4.\tPrint Top Element'
		x = int(raw_input("Choose Menu : "))

		if x == 1:
			s.push(str(raw_input("Input Stack : ")))

		elif x == 2:
			print  ('{0} popped from stack'.format(s.pop()))

		elif x == 3:
			print s
			if s.isEmpty() is True:
				print 'Stack is Empty'

		elif x == 4:
			print "Top Element is " + s.peek()
			if s.isEmpty() is True:
				print 'Stack is Empty'

		else:
			break

if __name__ == '__main__':
	main()

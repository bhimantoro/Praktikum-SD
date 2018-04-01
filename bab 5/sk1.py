import os
class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next

class Counter(object):
	__count=0

	def itung(self):
		self.__count += 1
		print 'Nomor Antrian = ' + str(self.__count)

count = Counter()

class waktuAntri(object):
	__time = 0

	def ngantri(self):
		self.__time += 10
		print 'Harap Menunggu ' + str(self.__time) + ' Menit'

antri = waktuAntri()

class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

	def insert(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node


	def size(self):
		current = self.head
		count = 0
		while current:
			count += 1
			current = current.get_next()
		return count

	# def search(self, data):
	# 	current = self.head
	# 	found = False
	# 	while current and found is False:
	# 		if current.get_data() == data:
	# 			found = True
	# 		else:
	# 			current = current.get_next()
	# 	return found
	#
	# def delete(self, data):
	# 	current = self.head
	# 	previous = None
	# 	found = False
	# 	while current and found is False:
	# 		if current.get_data() == data:
	# 			found = True
	# 		else:
	# 			previous = current
	# 			current = current.get_next()
	# 	if current is None:
	# 		raise ValueError("Data not in list")
	# 	if previous is None:
	# 		self.head = current.get_next()
	# 	else:
	# 		previous.set_next(current.get_next())
	#
	# def showData(self):
	# 	os.system('cls')
	# 	print ("Tampilkan list data:")
	# 	print ("Node -> Next Node")
	# 	current_node = self.head
	# 	while current_node is not None:
	# 		print (current_node.data),
	# 		print (" ->"),
	# 		print (current_node.next_node.data) if hasattr(current_node.next_node, "data") else None
	# 		current_node = current_node.next_node

	def mainmenu(self):
		pilih = "y"
		while (pilih == "y"):
			print("==============================")
			print("| Antri Pasien Rumah Sakit Y |")
			print("==============================")
			print("1. Tambah Pasien")
			print("2. Jumlah Antrian")
			print("===============================")
			pilihan=str(raw_input("Silakan masukan pilihan anda: "))
			if(pilihan=="1"):
				obj = str(raw_input("Masukan Data Pasien: "))
				self.insert(obj)
				str(count.itung())
				str(antri.ngantri())
				print 'Dari Total Antrian ' + str(self.size())
			elif(pilihan=="2"):
				print("Jumlah Antrian Pasien : "+str(self.size()))
				os.system("pause")
			else: pilih="n"

if __name__ == '__main__':
	l = LinkedList()
	l.mainmenu()

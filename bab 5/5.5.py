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

	def search(self, data):
		current = self.head
		found = False
		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				current = current.get_next()
		return found

	def delete(self, data):
		current = self.head
		previous = None
		found = False
		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				previous = current
				current = current.get_next()
		if current is None:
			raise ValueError("Data not in list")
		if previous is None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())

	def showData(self):
		os.system('cls')
		print ("Tampilkan list data:")
		print ("Node -> Next Node")
		current_node = self.head
		while current_node is not None:
			print (current_node.data),
			print (" ->"),
			print (current_node.next_node.data) if hasattr(current_node.next_node, "data") else None

			current_node = current_node.next_node

	def mainmenu(self):
		pilih = "y"
		while (pilih == "y"):
			os.system("cls")
			print("===============================")
			print("| Menu aplikasi linked list |")
			print("===============================")
			print("1. Insert data")
			print("2. Delete data")
			print("3. Cari data")
			print("4. Panjang dari linked list")
			print("5. Tampil data")
			print("===============================")
			pilihan=str(raw_input("Silakan masukan pilihan anda: "))
			if(pilihan=="1"):
				os.system("cls")
				obj = str(raw_input("Masukan data yang ingin anda tambahkan: "))
				self.insert(obj)
			elif(pilihan=="2"):
				os.system("cls")
				obj = str(raw_input("Masukan data yang ingin anda dihapus: "))
				self.delete(obj)
				x = raw_input("")
			elif(pilihan=="3"):
				os.system("cls")
				obj = str(raw_input("Masukan data yang ingin anda dicari: "))
				status = self.search(obj)
				if status == True:
					print("Data ditemukan pada list")
				else:
					print("Data tidak ditemukan")
				x = raw_input("")
			elif(pilihan=="4"):
				os.system("cls")
				print("Panjang dari queue adalah: "+str(self.size()))
				x = raw_input("")
			elif(pilihan=="5"):
				os.system("cls")
				self.showData()
				x = raw_input("")
			else: pilih="n"

if __name__ == '__main__':
	l = LinkedList()
	l.mainmenu()

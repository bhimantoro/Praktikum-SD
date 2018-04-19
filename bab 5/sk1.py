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

	def mainmenu(self):
		while True:
			try:
				print("==============================")
				print("| Antri Pasien Rumah Sakit Y |")
				print("==============================")
				print("1. Tambah Pasien")
				print("2. Jumlah Antrian")
				print("===============================")
				pilihan = str(raw_input("Silakan masukan pilihan anda: "))
				if pilihan == "1":
					obj = str(raw_input("Masukan Data Pasien: "))
					self.insert(obj)
					print 'Silahkan menunggu ', (self.size() - 1) * 10, ' menit'
					print 'Dari Total Antrian ', (self.size() - 1) + 1
				elif pilihan == "2":
					print("Jumlah Antrian Pasien : " + str(self.size()))
					os.system("pause")
				else:
					print("Pilihan salah")
					os.system("pause")
			except:
				continue

if __name__ == '__main__':
	l = LinkedList()
	l.mainmenu()

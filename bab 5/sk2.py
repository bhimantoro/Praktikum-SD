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
        print ("Tampilkan list data:")
        current_node = self.head
        while current_node is not None:
            print (current_node.data),
            print ("   ->"),
            print (current_node.next_node.data) if hasattr(current_node.next_node, "data") else None
            current_node = current_node.next_node

l = LinkedList()
d = LinkedList()
while True:
    print("===============================")
    print("| Menu aplikasi linked list |")
    print("===============================")
    print("1. Insert data")
    print("2. Delete data")
    print("3. Tampilkan List")
    print("4. Exit")
    print("===============================")
    pilihan=str(input(("Silakan masukan pilihan anda: ")))
    if(pilihan=="1"):
        print("    1. Insert Pembayar DP")
        print("    2. Insert Pembayar Lunas")
        pilihanw=str(input(("====Silakan masukan pilihan anda: ")))
        if(pilihanw=="1"):
            obj = str(raw_input("====Masukan data yang ingin anda tambahkan: "))
            d.insert(obj)
        else:
            obj = str(raw_input("====Masukan data yang ingin anda tambahkan: "))
            l.insert(obj)
        x = raw_input("")

    elif(pilihan=="2"):
        print("    1. Remove yang Lunas")
        print("    2. Remove Data pemesan tertentu")
        pilihanw=str(raw_input(("====Silakan masukan pilihan anda: ")))
        if(pilihanw=="1"):
            if l.head != None:
                print "====",l.head.data , "Telah Dihapus"
                l.delete(l.head.data)
            else:
                print("====Data tidak ditemukan")

        else :
            obj = str(raw_input("====Masukan data yang ingin dihapus:"))
            status = d.search(obj)
            if status == True:
                d.delete(obj)
                print "====",obj , "Telah Dihapus"
            else:
                print("====Data tidak ditemukan")
        x = raw_input("")

    elif(pilihan=="3"):
        print("    1. Data Pembayar DP")
        print("    2. Data Pembayar Lunas")
        pilihanw=str(input(("Silakan masukan pilihan anda: ")))
        if(pilihanw=="1"):
            d.showData()
        else:
            l.showData()
        x = raw_input("")
    elif(pilihan=="4"):
        exit()
    else :
        print "Input Error Back to Menu"
        x = raw_input("")
        continue

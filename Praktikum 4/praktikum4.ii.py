#============================================
#Nama: Fardhan Al Biansya
#NIM: J0403251060
#Kelas: B1
#============================================

#============================================
#Implementasi Dasar : Node pada Linked List
#============================================

class Node:
    def __init__(self, data):
        self.data = data      # ✅ simpan data
        self.next = None

# 1) Membuat node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) Menghubungkan Node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

# 3) Menentukan node pertama (head)
head = nodeA

# 4) Traversal
current = head
while current is not None:
    print(current.data)
    current = current.next

print("===List Baru===")

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_awal(self, data):
        nodeBaru = Node(data)
        nodeBaru.next = self.head
        self.head = nodeBaru
    
    def tampilkan(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def hapus_awal(self):
        if self.head is None:
            print("List kosong")
            return
        data_terhapus = self.head.data
        self.head = self.head.next
        print("Node yang dihapus adalah:", data_terhapus)

ll = LinkedList()
ll.insert_awal("X") 
ll.insert_awal("Y") 
ll.insert_awal("Z")  
ll.tampilkan()
ll.hapus_awal()
ll.tampilkan()
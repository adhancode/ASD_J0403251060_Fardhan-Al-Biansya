#============================================
#Nama: Fardhan Al Biansya
#NIM: J0403251060
#Kelas: B1
#============================================

#============================================
#Implementasi Dasar : Node pada Linked List
#============================================

# Membuat class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue dengan 2 pointer (front dan rear)
class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        # Menambah data di belakang (rear)
        nodeBaru = Node(data)

        # Jika queue kosong
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        # Jika queue tidak kosong
        self.rear.next = nodeBaru
        self.rear = nodeBaru 

    def dequeue(self):
        # Menghapus data di depan (front)

        #1) Ambil data yang akan paling depan
        data_terhapus = self.front.data

        #2) Geser front ke node berikutnya
        self.front = self.front.next

        #3) Jika setelah di-dequeue queue menjadi kosong, set rear ke None
        if self.front is None:
            self.rear = None

        print("Data yang di-dequeue adalah:", data_terhapus)
        return data_terhapus

    def tampilkan(self):
        current = self.front
        print("Front -> ", end="")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None (Rear <- Rear")

#============================================

# Instansiasi objek QueueLL
q = QueueLL()

q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()

q.dequeue()
q.tampilkan()
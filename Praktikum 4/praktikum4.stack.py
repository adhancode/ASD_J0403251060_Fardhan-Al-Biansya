#============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B1
#============================================

# ===========================================
# Implementasi Stack (LIFO) Berbasis Linked List
# ===========================================

class Node:
    def __init__(self, data):
        self.data = data      # Menyimpan nilai/data pada node
        self.next = None      # Pointer ke node berikutnya (Default None)


class Stack:
    def __init__(self):
        self.top = None       # Menunjuk node paling atas (Awal stack kosong)

    def is_empty(self):
        return self.top is None   # Mengembalikan True jika stack kosong

    def push(self, data):
        node_baru = Node(data)    # Membuat node baru

        node_baru.next = self.top # Node baru menunjuk ke top lama

        self.top = node_baru      # Memindahkan top ke node baru

    def pop(self):
        if self.is_empty():       # Mengecek apakah stack kosong
            print("Stack kosong, tidak bisa pop.")
            return None

        data_terambil = self.top.data  # Menyimpan data dari node paling atas
        self.top = self.top.next       # Menggeser top ke node berikutnya
        return data_terambil           # Mengembalikan data yang dihapus

    def peek(self):
        if self.is_empty():       # Mengecek apakah stack kosong
            return None
        return self.top.data      # Mengembalikan data paling atas tanpa menghapus

    def tampilkan(self):
        current = self.top        # Memulai dari node paling atas
        print("Top -> ", end="")  # Menampilkan penanda awal stack

        while current is not None:        # Selama masih ada node
            print(current.data, end=" -> ")  # Menampilkan data
            current = current.next          # Pindah ke node berikutnya

        print("None")             # Menampilkan penanda akhir stack

s = Stack()  # Membuat objek stack

s.push("A")  # Menambahkan A ke dalam stack
s.push("B")  # Menambahkan B ke dalam stack
s.push("C")  # Menambahkan C ke dalam stack

print("Isi stack setelah push A, B, C:")  # Menampilkan keterangan
s.tampilkan()  # Menampilkan isi stack

print("Peek:", s.peek())  # Melihat elemen paling atas tanpa menghapus

data = s.pop()  # Menghapus elemen paling atas
print("Pop mengembalikan:", data)  # Menampilkan data yang dihapus

print("Isi stack setelah pop:")  # Menampilkan keterangan
s.tampilkan()  # Menampilkan isi stack setelah pop
# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# =============================================

# =============================================
# Latihan 2: Membuat Binary Search Tree sederhana
# =============================================

#Class Node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data    # Menyimpan data pada node
        self.left = None    # Child kiri, awalnya None
        self.right = None   # Child kanan, awalnya None

# Membuat Node Root
root = Node("A") # Membuat node root dengan data "A"

# Membuat Child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat Child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan isi node root dan childnya
print("Data pada root : ", root.data)                       # Output: A
print("Data Child kiri root : ", root.left.data)            # Output: B
print("Data Child kanan root : ", root.right.data)          # Output: C
print("Data Child kiri dari B : ", root.left.left.data)     # Output: D
print("Data Child kanan dari B : ", root.left.right.data)   # Output: E

# Pembahasan: 
'''
Kode di atas digunakan untuk membuat struktur node pada tree dengan 
menggunakan class Node. Di dalamnya terdapat fungsi __init__ yang 
berfungsi untuk menginisialisasi atribut data sebagai isi node, 
serta left dan right sebagai child kiri dan kanan yang awalnya bernilai None. 
Kemudian dibuat sebuah node root dengan root = Node("A") yang berisi data "A", 
lalu ditambahkan child level 1 yaitu "B" sebagai child kiri dan "C" sebagai 
child kanan. Setelah itu, ditambahkan lagi child level 2 pada node "B", 
yaitu "D" sebagai child kiri dan "E" sebagai child kanan. Selanjutnya, 
dilakukan print untuk menampilkan isi node, sehingga terlihat hubungan 
antar node dari root hingga child. Secara singkat, kode ini menunjukkan 
cara membuat struktur tree sederhana hingga beberapa level dan menampilkan isinya.
'''
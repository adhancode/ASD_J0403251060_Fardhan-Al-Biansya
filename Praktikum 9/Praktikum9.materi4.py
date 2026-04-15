# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# =============================================

# =============================================
# Latihan 4: Membuat Traversal Inorder
# =============================================

# Class Node digunakan untuk dasar dari Tree

class Node:
    def __init__(self, data):
        self.data = data    # Menyimpan data pada node
        self.left = None    # Child kiri, awalnya None
        self.right = None   # Child kanan, awalnya None

# Membuat Inorder: Left -> Root -> Right
def inorder(node):
    if node is not None:
        inorder(node.left)        # Kunjungi child kiri
        print(node.data, end=" ") # Kunjungi node saat ini
        inorder(node.right)       # Kunjungi child kanan

# Membuat Tree
# Membuat Node Root
root = Node("A")

# Membuat Child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat Child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan hasil Traversal Inorder
print("Hasil Traversal Inorder : ")
inorder(root) # Output: D B E A C

# Pembahasan:
'''
Kode di atas digunakan untuk membuat struktur tree sekaligus melakukan 
traversal dengan metode inorder menggunakan class Node. Di dalam class 
terdapat fungsi __init__ yang berfungsi untuk menginisialisasi atribut 
data sebagai isi node, serta left dan right sebagai child kiri dan kanan 
yang awalnya bernilai None. Selanjutnya dibuat fungsi inorder(node) yang 
bekerja dengan urutan left, root, lalu right, yaitu menelusuri child kiri 
terlebih dahulu, kemudian menampilkan data node, dan dilanjutkan ke child 
kanan secara rekursif. Setelah itu dibuat node root dengan root = Node("A"), 
lalu ditambahkan child "B" dan "C" pada level 1, serta "D" dan "E" pada level 2. 
Terakhir, fungsi inorder(root) dipanggil untuk menampilkan hasil traversal 
sehingga urutan yang dihasilkan adalah D B E A C. Secara singkat, kode ini 
menunjukkan cara membuat tree dan melakukan traversal inorder untuk menampilkan isi node.
'''
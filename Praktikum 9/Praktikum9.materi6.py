# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# =============================================

# =============================================
# Latihan 6: Stuktur Organisasi Perusahaan
# =============================================

# Class Node digunakan untuk dasar dari Tree

class Node:
    def __init__(self, data):
        self.data = data    # Menyimpan data pada node
        self.left = None    # Child kiri, awalnya None
        self.right = None   # Child kanan, awalnya None

def preorder(node):
    if node is not None:
        print(node.data, end=" ") # Menampilkan data pada node
        preorder(node.left)       # Traversal ke child kiri
        preorder(node.right)      # Traversal ke child kanan

# Membuat Tree Struktur Organisasi Perusahaan
root = Node("Direktur")

# Child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

# Child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")

root.right.left = Node("Staff 3")

# Menjalankan transversal preorder
print("Struktur Organisasi (preorder): ")
preorder(root)

# Pembahasan:
'''
Kode di atas digunakan untuk membuat struktur tree yang menggambarkan organisasi 
perusahaan sekaligus melakukan traversal preorder menggunakan class Node. 
Di dalam class terdapat fungsi __init__ yang berfungsi untuk menginisialisasi 
atribut data sebagai isi node, serta left dan right sebagai child kiri dan 
kanan yang awalnya bernilai None. Selanjutnya dibuat fungsi preorder(node) 
yang bekerja dengan urutan root, left, lalu right, yaitu menampilkan data 
terlebih dahulu, kemudian menelusuri child kiri dan dilanjutkan ke child kanan 
secara rekursif. Setelah itu dibuat node root "Direktur", lalu ditambahkan 
"Manajer A" dan "Manajer B" sebagai child level 1, serta beberapa staff sebagai 
child level 2. Terakhir, fungsi preorder(root) dipanggil untuk menampilkan 
struktur organisasi sesuai urutan preorder. Secara singkat, kode ini menunjukkan 
cara merepresentasikan struktur organisasi dalam bentuk tree dan menampilkannya 
dengan traversal preorder.
'''
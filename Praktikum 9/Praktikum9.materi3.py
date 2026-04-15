# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# =============================================

# =============================================
# Latihan 3: Membuat Traversal Preorder
# =============================================

#Class Node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data    # Menyimpan data pada node
        self.left = None    # Child kiri, awalnya None
        self.right = None   # Child kanan, awalnya None

# Fungsi Preorder : Root -> Left -> Right
def preorder(node):
    if node is not None:
        print(node.data, end=" ")   # Menampilkan data pada node
        preorder(node.left)         # Traversal ke child kiri
        preorder(node.right)        # Traversal ke child kanan

# Membuat Node Root
root = Node("A") # Membuat node root dengan data "A"

# Membuat Child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat Child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan hasil Traversal Preorder
print("Hasil Traversal Preorder : ")
preorder(root) # Output: A B D E C

# Pembahasan:
'''
Kode di atas digunakan untuk membuat struktur tree sekaligus melakukan 
traversal dengan metode preorder menggunakan class Node. Di dalam class 
terdapat fungsi __init__ yang berfungsi untuk menginisialisasi atribut 
data sebagai isi node, serta left dan right sebagai child kiri dan kanan 
yang awalnya bernilai None. Selanjutnya dibuat fungsi preorder(node) yang 
bekerja dengan urutan root, left, lalu right, yaitu menampilkan data node 
terlebih dahulu, kemudian menelusuri child kiri dan dilanjutkan ke child 
kanan secara rekursif. Setelah itu dibuat node root dengan root = Node("A"), 
lalu ditambahkan child "B" dan "C" pada level 1, serta "D" dan "E" pada level 2. 
Terakhir, fungsi preorder(root) dipanggil untuk menampilkan hasil traversal 
sehingga urutan yang dihasilkan adalah A B D E C. Secara singkat, kode ini 
menunjukkan cara membuat tree dan melakukan traversal preorder untuk menampilkan isi node.
'''
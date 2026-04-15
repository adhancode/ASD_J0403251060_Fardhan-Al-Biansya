# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# =============================================

# =============================================
# Latihan 5: Membuat Traversal Postorder
# =============================================

# Class Node digunakan untuk dasar dari Tree

class Node:
    def __init__(self, data):
        self.data = data    # Menyimpan data pada node
        self.left = None    # Child kiri, awalnya None
        self.right = None   # Child kanan, awalnya None

# Fungsi Postorder : Left -> Right -> Root
def postorder(node):
    if node is not None:
        postorder(node.left)      # Traversal ke child kiri
        postorder(node.right)     # Traversal ke child kanan
        print(node.data, end=" ") # Menampilkan data pada node

# Membuat Node Root
root = Node("A") # Membuat node root dengan data "A"

# Membuat Child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat Child level 2
root.left.left = Node("D")
root.left.right = Node("E")

# Menampilkan hasil Traversal Postorder
print("Hasil Traversal Postorder : ")
postorder(root) # Output: D E B C A

# Pembahasan:
'''
Kode di atas digunakan untuk membuat struktur tree sekaligus melakukan 
traversal dengan metode postorder menggunakan class Node. Di dalam class 
terdapat fungsi __init__ yang berfungsi untuk menginisialisasi atribut 
data sebagai isi node, serta left dan right sebagai child kiri dan kanan 
yang awalnya bernilai None. Selanjutnya dibuat fungsi postorder(node) 
yang bekerja dengan urutan left, right, lalu root, yaitu menelusuri child 
kiri terlebih dahulu, kemudian child kanan, dan terakhir menampilkan data 
node secara rekursif. Setelah itu dibuat node root dengan root = Node("A"), 
lalu ditambahkan child "B" dan "C" pada level 1, serta "D" dan "E" pada level 2. 
Terakhir, fungsi postorder(root) dipanggil untuk menampilkan hasil traversal 
sehingga urutan yang dihasilkan adalah D E B C A. Secara singkat, kode ini 
menunjukkan cara membuat tree dan melakukan traversal postorder untuk menampilkan isi node.
'''
# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# =============================================

# =============================================
# Latihan 4: Membuat BST yang Tidak Seimbang
# =============================================

# Class Node untuk menyimpan data BST
class Node:
    def __init__(self, data):
        self.data = data    # nilai pada node
        self.left = None    # child kiri
        self.right = None   # child kanan

# Fungsi insert untuk BST
# Alur: Jika root kosong, buat node baru. Jika data lebih kecil, masuk ke kiri. 
# Jika data lebih besar, masuk ke kanan.
def insert(root, data):
    # Jika root kosong, buat node baru
    if root is None:
        return Node(data)

    # Jika data lebih kecil, masuk ke subtree kiri
    if data < root.data:
        root.left = insert(root.left, data)
    
    # Jika data lebih besar, masuk ke subtree kanan
    elif data > root.data:
        root.right = insert(root.right, data)

    return root

# Fungsi preorder untuk melihat bentuk tree
# Alur: Kunjungi Root, lalu telusuri subtree kiri, kemudian subtree kanan.
def preorder(root):
    if root is not None:
        print(root.data, end=" ") # Menampilkan data
        preorder(root.left)       # Rekursif kiri
        preorder(root.right)      # Rekursif kanan

# Fungsi sederhana untuk menampilkan struktur tree
# Alur: Menampilkan data dengan indentasi sesuai level dan keterangan posisi (Root/L/R).
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print("  " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# ---------------------------------------------
# Program utama
# ---------------------------------------------
root = None

# Data dimasukkan berurutan naik
data_list = [10, 20, 30] #

for data in data_list:
    root = insert(root, data)

# Menampilkan hasil traversal preorder
print("Preorder BST:")
preorder(root) # Output: 10 20 30

# Menampilkan visualisasi struktur tree
print("\n\nStruktur BST:")
tampil_struktur(root)

# Pembahasan:
'''
Kode di atas digunakan untuk mendemonstrasikan pembuatan Binary Search Tree (BST) 
yang tidak seimbang menggunakan class Node. Di dalam class 
terdapat fungsi __init__ untuk inisialisasi data serta pointer left dan right. 
Fungsi insert bekerja dengan membandingkan nilai; namun karena data dimasukkan 
secara berurutan naik (10, 20, 30), setiap data baru selalu menjadi child kanan 
dari node sebelumnya. Hal ini menyebabkan tree condong ke kanan 
(right-skewed) sebagaimana terlihat pada fungsi tampil_struktur. 
Kondisi ini menunjukkan bahwa BST tidak selalu seimbang, dan semakin panjang 
tree yang condong seperti ini, maka proses pencarian data akan menjadi semakin 
lambat karena menyerupai Linked List. Secara singkat, kode ini menunjukkan 
pengaruh urutan input data terhadap efisiensi dan keseimbangan struktur BST.
'''
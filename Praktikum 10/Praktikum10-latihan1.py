# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# =============================================

# =============================================
# Latihan 1: BST
# =============================================

# Class Node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data    # Menyimpan data pada node
        self.left = None    # Child kiri, awalnya None
        self.right = None   # Child kanan, awalnya None

# Alur fungsi Insert pada BST
'''
Jika node kosong, buat node baru. 
Jika nilai data lebih kecil dari node saat ini, rekursif ke child kiri. 
Jika lebih besar, rekursif ke child kanan.
'''

def insert(root, data):
    if root is None:
        return Node(data)   # Membuat node baru jika kosong

    if data < root.data:
        root.left = insert(root.left, data)     # Insert ke child kiri
    elif data > root.data:
        root.right = insert(root.right, data)   # Insert ke child kanan
    return root

# Mengisi data BST
root = None
data_list = [50, 30, 70, 20, 40, 50, 80] # Catatan: Angka 50 yang kedua akan diabaikan oleh kondisi insert di atas

for data in data_list:
    root = insert(root, data)

# =============================================
# Latihan 2: Traversal Inorder
# =============================================

# Alur fungsi Inorder Traversal pada BST: 
'''Menelusuri child kiri terlebih dahulu (Left), 
mencetak data node saat ini (Root), 
lalu menelusuri child kanan (Right). Menghasilkan output terurut.
'''

def inorder(root):
    if root is not None:
        inorder(root.left)        # Kunjungi child kiri
        print(root.data, end=" ") # Kunjungi node saat ini
        inorder(root.right)       # Kunjungi child kanan

print("Hasil Inorder: ")
inorder(root) # Output: 20 30 40 50 70 80
print() # Menambahkan baris baru untuk kerapian output

# =============================================
# Latihan 3: Search di BST
# =============================================

# Alur fungsi Search pada BST: 
'''Jika root kosong kembalikan False. 
Jika nilai dicari sama dengan data node, kembalikan True. 
Jika lebih kecil cari di child kiri, jika lebih besar cari di child kanan.'''

def search(root, key):
    if root is None:
        return False        # Data tidak ditemukan sampai ujung leaf

    if root.data == key:
        return True         # Data ditemukan
    elif key < root.data:
        return search(root.left, key)   # Cari di child kiri
    else:
        return search(root.right, key)  # Cari di child kanan
    
# Uji Pencarian
key = 40

if search(root, key):
    print("Data ditemukan")         # Output: Data ditemukan
else:
    print("Data tidak ditemukan")
# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# =============================================

# =============================================
# Latihan 6: Rotasi Kanan pada BST Tidak Seimbang
# =============================================

class Node:
    def __init__(self, data):
        self.data = data    # Menyimpan data pada node
        self.left = None    # Child kiri, awalnya None
        self.right = None   # Child kanan, awalnya None

# Alur fungsi rotasi kanan: 
'''Menarik simpul anak kiri (x) ke atas menjadi root baru, 
dan menurunkan root lama (y) menjadi anak kanan dari root baru tersebut.'''

def rotasi_kanan(y):
    x = y.left        # x adalah anak kiri dari y
    T2 = x.right      # T2 adalah anak kanan dari x (jika ada)

    # Proses rotasi
    x.right = y       # Root lama (y) turun menjadi anak kanan dari x
    y.left = T2       # T2 berpindah menjadi anak kiri dari y

    # Mengembalikan x karena sekarang x adalah root yang posisinya paling atas
    return x

# Fungsi untuk mencetak tree secara Preorder (Root, Kiri, Kanan)
# Dipilih Preorder agar posisi root yang berubah terlihat dengan jelas
def cetak_preorder(root):
    if root is not None:
        print(root.data, end=" ")
        cetak_preorder(root.left)
        cetak_preorder(root.right)

# =============================================
# Program utama
# =============================================

# 1. Membuat tree yang miring ke kiri (Tidak Seimbang)
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

print("Sebelum Rotasi Kanan (Preorder):")
cetak_preorder(root) 
# Output: 30 20 10 (Artinya: 30 adalah root, 20 di kirinya, 10 di kiri 20)
print("\n")

# 2. Melakukan proses rotasi kanan pada root
root = rotasi_kanan(root)

print("Sesudah Rotasi Kanan (Preorder):")
cetak_preorder(root) 
# Output: 20 10 30 (Artinya: 20 sekarang menjadi root, 10 di kirinya, 30 di kanannya)
print()
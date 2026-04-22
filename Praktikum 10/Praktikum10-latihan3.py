# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# =============================================

# =============================================
# Latihan 5: Rotasi Kiri pada BST Tidak Seimbang
# =============================================

class Node:
    def __init__(self, data):
        self.data = data    # Menyimpan data pada node
        self.left = None    # Child kiri, awalnya None
        self.right = None   # Child kanan, awalnya None

# Alur fungsi preorder: Menampilkan data mulai dari root, lalu ke kiri, baru ke kanan.
def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Alur fungsi tampil_struktur: Mencetak bentuk pohon dengan spasi agar terlihat tingkatannya.
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:
        print("  " * level + f"{posisi}: {root.data}")
        tampil_struktur(root.left, level + 1, "L")
        tampil_struktur(root.right, level + 1, "R")

# Alur fungsi rotasi kiri: Menggeser posisi node agar pohon yang miring ke kanan jadi lebih rapi.
def rotate_left(x):
    # x adalah root yang lama
    y = x.right         # y jadi calon root baru
    T2 = y.left         # simpan sementara cabang kiri y

    # Proses tukar posisi
    y.left = x          
    x.right = T2        

    return y  # Kembalikan y sebagai root yang baru

# ----------------------------
# Program utama
# ----------------------------
# Buat pohon yang miring ke kanan (10 -> 20 -> 30)
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)

print("Preorder sebelum rotasi kiri:")
preorder(root) 

print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(root)

# Jalankan fungsi rotasi kiri
root = rotate_left(root)

print("\nPreorder sesudah rotasi kiri:")
preorder(root) 

print("\n\nStruktur sesudah rotasi kiri:")
tampil_struktur(root)

# Pembahasan:
'''
Kode di atas dibuat untuk mempraktikkan cara memutar posisi node pada 
Binary Search Tree (BST) yang tidak seimbang lewat fungsi rotasi kiri. 
Di dalam class Node, ada fungsi __init__ yang menyiapkan tempat untuk data 
dan penghubung ke node lain (kiri dan kanan). Awalnya, kita membuat pohon 
yang miring ke kanan dengan urutan angka 10, 20, dan 30. Karena bentuknya 
hanya memanjang ke satu sisi, pohon ini jadi kurang efisien. Untuk memperbaikinya, 
digunakan fungsi rotate_left yang menaikkan posisi node 20 menjadi root 
dan menggeser node 10 ke posisi sebelah kiri. Hasilnya bisa dilihat lewat 
fungsi preorder dan tampil_struktur, di mana posisi angka-angkanya berubah 
jadi lebih rata dan rapi. Secara singkat, kode ini menunjukkan bahwa rotasi 
bisa digunakan untuk merapikan struktur pohon agar pencarian data nantinya 
bisa berjalan lebih cepat.
'''
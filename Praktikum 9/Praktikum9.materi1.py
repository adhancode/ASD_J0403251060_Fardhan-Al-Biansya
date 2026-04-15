# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# =============================================

# =============================================
# Latihan 1: Membuat Node
# =============================================

#Class Node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data    # Menyimpan data pada node
        self.left = None    # Child kiri, awalnya None
        self.right = None   # Child kanan, awalnya None

#Membuat sebuah node root
root = Node("A")

#Menampilkan isi node
print("Data pada root", root.data)          #Output: A
print("Data child kiri root", root.left)    #Output: None
print("Data child kanan root", root.right)  #Output: None

#Pembahasan:
'''
Kode di atas digunakan untuk membuat struktur dasar node pada tree dengan 
menggunakan class Node. Di dalamnya terdapat fungsi init yang berfungsi 
untuk menginisialisasi atribut data sebagai isi node, serta left dan right 
sebagai child kiri dan kanan yang nilainya masih None karena belum terhubung 
dengan node lain. Kemudian dibuat sebuah node root dengan root = Node("A") 
yang berisi data "A". Setelah itu, dilakukan print untuk menampilkan isi node, 
sehingga terlihat bahwa data pada root adalah "A", sedangkan child kiri dan 
kanan masih kosong. Secara singkat, kode ini menunjukkan cara sederhana membuat 
satu node pada tree dan menampilkan isinya.
'''
# ==========================================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# ==========================================================
# Materi 1: Implementasi Algoritma Kruskal
# ==========================================================

# Daftar edge dengan format: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),  # Edge C-D dengan bobot 1
    (2, 'A', 'C'),  # Edge A-C dengan bobot 2
    (3, 'B', 'D'),  # Edge B-D dengan bobot 3
    (4, 'A', 'B'),  # Edge A-B dengan bobot 4
    (5, 'A', 'D')   # Edge A-D dengan bobot 5
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

# List untuk menyimpan hasil MST
mst = []

# Variabel untuk menyimpan total bobot
total_weight = 0

# Set untuk menyimpan node yang sudah terhubung
connected = set()

# Memeriksa setiap edge
for weight, u, v in edges:

    # Jika edge tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        # Menambahkan edge ke MST
        mst.append((u, v, weight))

        # Menambahkan total bobot
        total_weight += weight

        # Menandai node sudah terhubung
        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

# Menampilkan edge yang dipilih
for edge in mst:
    print(edge)

# Menampilkan total bobot
print("Total bobot =", total_weight)

'''
Penjelasan:
Program ini menggunakan algoritma Kruskal sederhana
untuk mencari Minimum Spanning Tree (MST).

Program akan mengurutkan edge dari bobot terkecil,
lalu memilih edge yang tidak membentuk cycle.

Edge yang dipilih:
C-D = 1
A-C = 2
B-D = 3

Total bobot MST adalah 6.
'''
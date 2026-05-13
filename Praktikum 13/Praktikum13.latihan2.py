# ==========================================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# ==========================================================
# Latihan 2: Implementasi Sederhana Algoritma Kruskal 
# ==========================================================

# Membuat daftar edge beserta bobot
# Format data: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge dari bobot terkecil
edges.sort()

# Menyimpan hasil MST
mst = []

# Menyimpan total bobot
total_weight = 0

# Menyimpan node yang sudah terhubung
connected = set()

# Perulangan untuk memeriksa setiap edge
for weight, u, v in edges:

    # Memeriksa apakah edge membentuk cycle sederhana
    if u not in connected or v not in connected:

        # Menambahkan edge ke MST
        mst.append((u, v, weight))

        # Menambahkan bobot ke total bobot
        total_weight += weight

        # Menandai node sudah terhubung
        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    # Menampilkan edge yang dipilih
    print(edge)

# Menampilkan total bobot MST
print("Total bobot =", total_weight)


'''
Pertanyaan Analisis:
1. Edge mana yang dipilih pertama kali?
2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
3. Berapa total bobot MST yang dihasilkan?
4. Mengapa edge tertentu tidak dipilih?

Jawaban:
1. Edge C-D dengan bobot 1 dipilih pertama kali karena memiliki bobot paling kecil.
2. Karena algoritma Kruskal mencari total bobot minimum sehingga edge terkecil dipilih lebih dahulu.
3. Total bobot MST yang dihasilkan adalah 6.
4. Karena edge tersebut dapat membentuk cycle atau tidak diperlukan lagi.
'''
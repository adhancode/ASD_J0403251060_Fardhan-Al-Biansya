# ==========================================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# ==========================================================
# Latihan 1: Memahami Konsep Spanning Tree
# ==========================================================

# Membuat daftar edge pada graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Membuat contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Menampilkan seluruh edge graph
print("Edge pada graph:")
for edge in edges:
    # Menampilkan edge satu per satu
    print(edge)

# Menampilkan spanning tree
print("\nSpanning Tree:")
for edge in spanning_tree:
    # Menampilkan edge spanning tree
    print(edge)

# Menampilkan jumlah edge graph
print("\nJumlah edge graph =", len(edges))

# Menampilkan jumlah edge spanning tree
print("Jumlah edge spanning tree =", len(spanning_tree))


'''
Pertanyaan Analisis:
1. Apa perbedaan graph awal dan spanning tree?
2. Mengapa spanning tree tidak boleh memiliki cycle?
3. Mengapa jumlah edge spanning tree selalu lebih sedikit?

Jawaban:
1. Graph awal memiliki lebih banyak edge dan masih terdapat cycle. Sedangkan spanning tree hanya menggunakan edge yang diperlukan untuk menghubungkan semua node tanpa cycle.
2. Karena cycle membuat hubungan menjadi berulang dan membuat graph menjadi tidak efisien.
3. Karena spanning tree hanya mengambil edge yang diperlukan untuk menghubungkan seluruh node.
'''
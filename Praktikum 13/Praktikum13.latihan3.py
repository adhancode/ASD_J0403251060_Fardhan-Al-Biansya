# ==========================================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# ==========================================================
# Latihan 3: Implementasi Algoritma Prim
# ==========================================================

# Mengimpor library heapq
import heapq

# Membuat weighted graph
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# Membuat fungsi algoritma Prim
def prim(graph, start):

    # Menyimpan node yang sudah dikunjungi
    visited = set([start])

    # Menyimpan kandidat edge
    edges = []

    # Memasukkan edge dari node awal
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    # Menyimpan hasil MST
    mst = []

    # Menyimpan total bobot
    total_weight = 0

    # Perulangan selama edge masih ada
    while edges:

        # Mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        # Jika node belum dikunjungi
        if v not in visited:

            # Menambahkan node ke visited
            visited.add(v)

            # Menambahkan edge ke MST
            mst.append((u, v, weight))

            # Menambahkan total bobot
            total_weight += weight

            # Memeriksa node tetangga
            for neighbor, w in graph[v].items():

                # Jika neighbor belum dikunjungi
                if neighbor not in visited:

                    # Menambahkan edge baru ke heap
                    heapq.heappush(edges, (w, v, neighbor))

    # Mengembalikan hasil MST dan total bobot
    return mst, total_weight

# Menjalankan algoritma Prim mulai dari node A
mst, total = prim(graph, 'A')

# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    # Menampilkan edge yang dipilih
    print(edge)

# Menampilkan total bobot
print("Total bobot =", total)


'''
Pertanyaan Analisis:
1. Node awal apa yang digunakan?
2. Edge mana yang dipilih pertama kali?
3. Bagaimana Prim menentukan edge berikutnya?
4. Berapa total bobot MST yang dihasilkan?
5. Apa perbedaan pendekatan Prim dan Kruskal?

Jawaban:
1. Node awal yang digunakan adalah node A.
2. Edge A-C dipilih pertama kali karena memiliki bobot paling kecil dari node A.
3. Prim memilih edge dengan bobot paling kecil yang terhubung dengan node yang sudah dikunjungi.
4. Total bobot MST yang dihasilkan adalah 6.
5. Prim membangun tree dari satu node awal sedangkan Kruskal memilih edge terkecil secara global.
'''
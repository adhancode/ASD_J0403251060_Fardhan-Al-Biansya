# ==========================================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# Praktikum 12 - Graph II: Shortest Path 
# ==========================================================

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Membuat weighted graph dengan bobot negatif
# Di sini ada bobot -2 dari C ke B
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node awal
    ke semua node menggunakan algoritma Bellman-Ford.
    """

    # Membuat dictionary untuk menyimpan jarak minimum
    # Semua node diisi nilai tak hingga terlebih dahulu
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Proses relaksasi dilakukan sebanyak jumlah node - 1
    # Tujuannya agar semua kemungkinan jalur bisa diperbarui
    for _ in range(len(graph) - 1):

        # Mengecek semua edge dalam graph
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Jika node sudah punya jarak (bukan tak hingga)
                # dan ditemukan jalur yang lebih kecil
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    
                    # Update jarak ke neighbor
                    distances[neighbor] = distances[node] + weight

    # Mengembalikan hasil jarak terpendek
    return distances

# Menjalankan algoritma dari node A
hasil = bellman_ford(graph, 'A')

# Menampilkan hasil
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

'''
Pertanyaan Analisis:
1. Berapa bobot langsung dari A ke B?
2. Berapa total bobot jalur A -> C -> B?
3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
5. Apa yang dimaksud dengan proses relaksasi edge?
6. Apa perbedaan utama Bellman-Ford dan Dijkstra?

Jawaban:
1. Bobot langsung dari A ke B adalah 5.
2. Total bobot jalur A -> C -> B adalah 4 + (-2) = 2.
3. Jalur yang lebih kecil adalah A -> C -> B dengan total bobot 2.
4. Bellman-Ford bisa digunakan pada bobot negatif karena tidak langsung memilih jalur terbaik,
   tetapi mengecek semua kemungkinan jalur secara berulang.
5. Relaksasi edge adalah proses memperbarui jarak jika ditemukan jalur yang lebih kecil.
6. Perbedaannya, Dijkstra lebih cepat tetapi tidak bisa untuk bobot negatif,
   sedangkan Bellman-Ford lebih lambat tetapi bisa menangani bobot negatif.
'''
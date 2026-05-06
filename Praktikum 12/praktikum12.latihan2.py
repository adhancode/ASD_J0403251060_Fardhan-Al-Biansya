# ==========================================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# Praktikum 12 - Graph II: Shortest Path 
# ==========================================================

# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================

import heapq

# Membuat weighted graph dengan bobot positif
# Setiap node menyimpan tetangga dan bobot menuju node tersebut
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    # Membuat dictionary untuk menyimpan jarak minimum dari start ke semua node
    # Semua jarak awal diisi tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Priority queue digunakan untuk menyimpan node dengan jarak terkecil
    # Format isi queue adalah (jarak, node)
    priority_queue = [(0, start)]

    # Proses berjalan selama priority queue masih berisi data
    while priority_queue:
        # Mengambil node dengan jarak paling kecil
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak sekarang lebih besar dari jarak yang sudah tercatat,
        # maka node ini tidak perlu diproses lagi
        if current_distance > distances[current_node]:
            continue

        # Memeriksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Menghitung jarak baru dari start ke tetangga melalui node sekarang
            distance = current_distance + weight

            # Jika jarak baru lebih kecil, maka jarak diperbarui
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    # Mengembalikan jarak terpendek dari node awal ke semua node
    return distances

# Menjalankan fungsi Dijkstra dari node A
hasil = dijkstra(graph, 'A')

# Menampilkan hasil jarak terpendek dari node A
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)

'''
Pertanyaan Analisis:
1. Berapa jarak terpendek dari A ke B?
2. Berapa jarak terpendek dari A ke C?
3. Berapa jarak terpendek dari A ke D?
4. Mengapa jarak A ke D lebih kecil melalui C dibandingkan melalui B?
5. Apa fungsi priority_queue dalam algoritma Dijkstra?
6. Mengapa Dijkstra tidak cocok untuk graph dengan bobot negatif?

Jawaban:
1. Jarak terpendek dari A ke B adalah 4.
2. Jarak terpendek dari A ke C adalah 2.
3. Jarak terpendek dari A ke D adalah 3.
4. Karena jalur A -> C -> D memiliki total bobot 2 + 1 = 3, sedangkan A -> B -> D memiliki total bobot 4 + 5 = 9.
5. Priority queue berfungsi untuk memilih node dengan jarak sementara paling kecil lebih dulu.
6. Dijkstra tidak cocok untuk graph berbobot negatif karena hasil jarak yang sudah dipilih bisa berubah jika ada bobot negatif.
'''
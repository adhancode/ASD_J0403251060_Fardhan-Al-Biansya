# ==========================================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# Praktikum 12 - Graph II: Shortest Path 
# ==========================================================

# ==========================================================
# Materi 1: Algoritma Dijkstra
# ==========================================================

import heapq    # Mengambil pustaka heapq untuk membuat antrean prioritas

# Membuat graph berbobot menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},  # Titik A terhubung ke B (bobot 4) dan C (bobot 2)
    'B': {'D': 5},          # Titik B terhubung ke D (bobot 5)
    'C': {'D': 1},          # Titik C terhubung ke D (bobot 1)
    'D': {}                 # Titik D tidak terhubung ke mana-mana
}

def dijkstra(graph, start):
    # Menyiapkan tempat simpan jarak, awalnya semua dianggap tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari titik awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Membuat priority queue untuk memproses node dengan jarak terkecil
    pq = [(0, start)]

    while pq: # Terus berjalan selama antrean masih ada isinya
        # Mengambil titik dengan jarak paling pendek saat ini
        current_distance, current_node = heapq.heappop(pq)

        # Memeriksa semua tetangga dari titik yang sedang diproses
        for neighbor, weight in graph[current_node].items():
            
            # Menjumlahkan jarak saat ini dengan bobot ke tetangga
            distance = current_distance + weight

            # Jika jalur baru ini lebih pendek dari yang sudah dicatat
            if distance < distances[neighbor]:
                
                # Memperbarui catatan jarak dengan nilai yang lebih kecil[cite: 1]
                distances[neighbor] = distance

                # Memasukkan titik tersebut ke antrean untuk dicek tetangganya[cite: 1]
                heapq.heappush(pq, (distance, neighbor))

    return distances  # Mengembalikan hasil akhir jarak terpendek[cite: 1]

# Memanggil fungsi dan mencetak hasilnya ke layar
hasil = dijkstra(graph, 'A')
print(hasil)

'''
Penjelasan:
• Jarak dari A ke A = 0  
• Jarak dari A ke B = 4  
• Jarak dari A ke C = 2  
• Jarak dari A ke D = 3 
Karena A ➔  C ➔  D = 2 + 1 = 3 

Kelemahan utama algoritma Dijkstra adalah algoritma ini tidak dapat bekerja dengan benar 
pada graph yang memiliki bobot negatif. Dijkstra menggunakan pendekatan greedy dengan 
asumsi bahwa jarak terpendek yang sudah dipilih tidak akan berubah lagi, sehingga jika 
terdapat edge dengan bobot negatif, algoritma dapat menghasilkan perhitungan shortest path 
yang salah. Selain itu, pada graph yang sangat besar dengan jumlah node dan edge yang 
banyak, proses perhitungan juga dapat menjadi lebih kompleks dan membutuhkan 
penggunaan struktur data tambahan seperti priority queue agar tetap efisien. 
Contoh kelemahan algoritma Dijkstra dapat dilihat pada graph yang memiliki bobot negatif. 
Misalnya, terdapat jalur  
A ➔ B dengan bobot 5,  
A ➔ C dengan bobot 4,  
C ➔  B dengan bobot -3.  

Secara logika, jalur terpendek dari A ke B seharusnya melalui C, yaitu 4 + (-3) = 1. Namun, 
algoritma Dijkstra dapat langsung memilih jalur A ➔ B dengan bobot 5 lebih awal dan 
menganggapnya sebagai jalur terbaik, sehingga hasil shortest path menjadi tidak akurat.
'''
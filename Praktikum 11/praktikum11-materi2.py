# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# =============================================

# =============================================
# Materi 2: Implementasi BFS
# =============================================

#struktur data untuk membuat antrian, kita gunakan dari library collections bawaan Phyton
from collections import deque

#representasi graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def bfs(graph,start):
    #Fungsi untuk melakukan penelusuran graph dengan BFS
        #graph : dictionary yang menyimpan struktur dari graph
        #start : node awal penelusuran

    #Queue digunakan untuk menyimpan node yang akan diproses / dibaca
    queue = deque()

    #variabel yang digunakan untuk menyimpan node yang sudah diproses/sudah dikunjungi
    visited = set()

    #Masukkan node awal ke dalam queue
    queue.append(start)

    #tandai bahwa node awal sudah dikunjungi
    visited.add(start)

    while queue:
        #mengambil node paling depan dari queue
        node = queue.popleft()

        #Tampilkan node yang sedang diproses
        print(node, end=" ")

        #periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]:
            #jika tetangga belum dikunjungi
            if neighbor not in visited:
                #tandai sebagai sudah dikunjungi
                visited.add(neighbor)
                #Masukkan tetangga ke  queue untuk diproses nanti
                queue.append(neighbor)

#Menjalankan fungsi BFS dengan node 'A'
bfs(graph,'A')

'''
Penjelasan:
Kode ini menerapkan metode Breadth First Search (BFS) menggunakan bantuan library deque untuk 
mengatur antrean data secara efisien. Secara teknis, program bekerja dengan cara mengunjungi titik 
awal (node A) terlebih dahulu, lalu memasukkan semua tetangga langsungnya ke dalam antrean untuk 
diproses secara berurutan sesuai level kedalamannya. Penggunaan variabel `visited` sangat penting 
agar program tidak terjebak dalam perulangan yang sama dan memastikan setiap titik hanya dibaca 
satu kali. Hasil akhirnya adalah urutan penelusuran yang bergerak melebar, di mana semua titik pada 
satu tingkat diselesaikan terlebih dahulu sebelum berpindah ke tingkat berikutnya, sehingga menghasilkan 
urutan kunjungan yang sistematis dan rapi.
'''
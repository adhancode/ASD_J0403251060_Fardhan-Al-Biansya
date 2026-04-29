# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# =============================================

# =============================================
# Latihan 1: Studi Kasus BFS (Jalur Terdekat Lokasi)
# =============================================

#representasi graph
graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

#struktur data untuk membuat antrian, kita gunakan dari library collections bawaan Python
from collections import deque

def bfs(graph, start):
    #Fungsi untuk melakukan penelusuran graph dengan BFS
    #graph : dictionary yang menyimpan struktur dari graph
    #start : node awal penelusuran

    #variabel yang digunakan untuk menyimpan node yang sudah diproses/sudah dikunjungi
    visited = set()
    
    #Queue digunakan untuk menyimpan node yang akan diproses / dibaca,
    #sekaligus langsung memasukkan node awal ke dalam queue
    queue = deque([start])

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
                #Masukkan tetangga ke queue untuk diproses nanti
                queue.append(neighbor)

print("BFS dari Rumah:")
#Menjalankan fungsi BFS dengan node 'Rumah'
bfs(graph, 'Rumah')

'''
Penjelasan:
Program ini mensimulasikan pencarian lokasi terdekat dari "Rumah" menggunakan metode BFS yang 
bekerja dengan cara menyisir semua lokasi setingkat demi setingkat secara melebar. Awalnya, 
lokasi seperti "Sekolah" dan "Toko" dimasukkan ke dalam antrean *deque* sebagai prioritas pertama 
karena keduanya terhubung langsung dengan rumah. Setelah itu, program akan memproses satu per satu 
lokasi tersebut sambil mengecek tujuan selanjutnya, seperti "Perpustakaan" dari sekolah atau "Pasar" 
dari toko, tanpa mengunjungi kembali lokasi yang sudah ditandai dalam variabel *visited*. Dengan 
cara ini, urutan lokasi yang muncul di layar mencerminkan tahapan perjalanan yang sistematis, 
di mana semua tempat pada jarak yang sama diselesaikan terlebih dahulu sebelum melangkah lebih 
jauh ke lokasi berikutnya.
'''

'''
1. Node mana yang dikunjungi pertama? 
Jawab: Node yang dikunjungi pertama kali adalah Rumah. Hal ini karena pemanggilan fungsi pada 
akhir kode adalah bfs(graph, 'Rumah'), yang menetapkan 'Rumah' sebagai node awal (start) untuk 
dimasukkan pertama kali ke dalam antrean (queue).

2. Mengapa BFS cocok untuk mencari jalur terdekat?
Jawab: Karena algoritma BFS bekerja dengan cara menelusuri graf secara melebar pada setiap 
levelnya, di mana semua node yang berjarak satu langkah dari titik awal akan diperiksa seluruhnya 
sebelum beralih ke node yang berjarak dua langkah, dan seterusnya.

3. Apa perbedaan urutan BFS jika struktur graph diubah? 
Jawab: Urutan BFS akan berubah jika struktur graph diubah, karena BFS mengikuti urutan penelusuran
'''
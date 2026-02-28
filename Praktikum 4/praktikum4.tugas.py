#============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B1
#============================================
# 
# ===========================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# ===========================================

# Class Node (Mewakili 1 data pelanggan)
class Node:
    def __init__(self, no, nama, servis):
        self.no = no            # Menyimpan nomor antrian
        self.nama = nama        # Menyimpan nama pelanggan
        self.servis = servis    # Menyimpan jenis servis
        self.next = None        # Pointer ke node berikutnya (awal = None)

# Class Queue Bengkel (Struktur Linked List)
class QueueBengkel:
    def __init__(self):
        self.front = None   # Node paling depan (yang akan dilayani)
        self.rear = None    # Node paling belakang (yang terakhir masuk)

    # Enqueue -> Tambah pelanggan ke belakang antrian
    def enqueue(self, no, nama, servis):
        new_node = Node(no, nama, servis)   # Membuat node baru

        if self.front is None:              # Jika antrian kosong
            self.front = new_node           # Front menunjuk ke node baru
            self.rear = new_node            # Rear juga menunjuk ke node baru
        else:
            self.rear.next = new_node       # Node terakhir menunjuk ke node baru
            self.rear = new_node            # Rear dipindah ke node baru

        print("Pelanggan berhasil ditambahkan ke antrian.\n")

    # Dequeue -> Layani pelanggan terdepan (FIFO)
    def dequeue(self):
        if self.front is None:              # Jika antrian kosong
            print("Antrian kosong! Tidak ada pelanggan.\n")
            return

        print("Melayani Pelanggan:")
        print("No Antrian :", self.front.no)
        print("Nama       :", self.front.nama)
        print("Servis     :", self.front.servis)
        print()

        self.front = self.front.next        # Front maju ke node berikutnya

        if self.front is None:              # Jika setelah dequeue antrian kosong
            self.rear = None                # Rear juga diset None

    # Menampilkan seluruh antrian
    def tampilkan(self):
        if self.front is None:              # Jika antrian kosong
            print("Antrian masih kosong.\n")
            return

        print("\n=== Daftar Antrian ===")

        current = self.front               # Mulai traversal dari front
        while current is not None:         # Selama node masih ada
            print("No Antrian :", current.no)
            print("Nama       :", current.nama)
            print("Servis     :", current.servis)
            print("------------------------")
            current = current.next         # Pindah ke node berikutnya

        print()

# Program Utama (Menu)
def main():
    q = QueueBengkel()   # Membuat objek queue

    while True:          # Perulangan menu
        print("=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":                              # Menu tambah pelanggan
            no = input("No Antrian : ")
            nama = input("Nama       : ")
            servis = input("Servis     : ")
            q.enqueue(no, nama, servis)               # Panggil enqueue

        elif pilih == "2":                            # Menu layani pelanggan
            q.dequeue()                               # Panggil dequeue

        elif pilih == "3":                            # Menu lihat antrian
            q.tampilkan()                             # Panggil tampilkan

        elif pilih == "4":                            # Menu keluar
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!\n")

# Menjalankan Program
if __name__ == "__main__":
    main()
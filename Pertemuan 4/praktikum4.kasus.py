#=============================================
#Nama: Fardhan Al Biansya
#NIM: J0403251060
#Kelas: B1
#=============================================

#=============================================
#Sistem Kasus: Sistem Antrian Layanan Akademik
#Implementasi Queue
#Enqueue : memindahkan pointer rear (nambah data baru dari belakang)
#Dequeue : memindahkan pointer front (menghapus data dari depan)
# Front -> A -> B -> C -> Rear
#=============================================

#1) Mendefiniskan Node (Unit dasar linked list)
class Node:
    def __init__(self, nim, nama):
        self.nim    = nim      #Menyimpan NIM Mahasiswa
        self.nama   = nama     #Menyimpan Nama Mahasiswa
        self.next   = None     #Pointer ke node berikutnya (default None)

#2) Mendefinisikamn Queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        #Ketika queue kosong maka front = rear = None
        return self.front is None
    
    def enqueue(self, nim, nama):
        nodeBaru = Node(nim, nama)
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        #Jika queue tidak kosong, maka data baru diletakkan setelah rear kemudian dijadikan sebagai rear
        nodeBaru = Node(nim, nama)
        self.rear.next = nodeBaru
        self.rear = nodeBaru

    #Menghapus data paling depan (memberikan layanan akademik)
    def dequeue(self):

        if self.is_empty():
            print("Antrian kosong, tidak ada yang bisa dilayani")
            return None
        
        #Lihat data bagian front, simpan di variabel data yang akan duhapus (dilayani)
        node_dilayani = self.front

        #Geser front ke next front
        self.front = self.front.next

        #Jika front menjadi None (data antrian terakhir yang dilayani), maka front = rear = None
        if self.front is None:
            self.rear = None

        return node_dilayani

    def tampilkan(self):
        print("Daftar Antrian Mahasiswa (Front -> Rear): ")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no += 1

#Program Utama
def main():
    
    #Instantiasi queue
    q = queueAkademik()
    
    while True:
        print("\n === Menu Antrian Layanan Akademik === ")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")
        
        pilihan = input("MPilih Menu (!-4) : ").strip()
        
        if pilihan == "1":
            nim = input("Masukkan NIM: ").strip()
            nama = input("Masukkan Nama: ").strip()
            
            q.enqueue(nim,nama)
            print("Mahasiswa Berhasil ditambahkan ke antrian")

        elif pilihan == "2":
            dilayani = q.dequeue()
            if dilayani is not None:
                print(f"Mahasiswa Dilayani : {dilayani.nim} - {dilayani.nama}")

        elif pilihan == "3":
            q.tampilkan()

        elif pilihan == "4":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak tersedia")

if __name__ == "__main__":
    main()
#=======================================================
#Tugas: Stok Barang Kantin
#=======================================================

#=======================================================
#Fungsi 1: Membuat Fungsi Load Data
#=======================================================

nama_file='stok_barang.txt'

def baca_data_barang(nama_file):
    data_dict = {} #Inisialisasi data dictionary

    try:
        with open(nama_file,"r", encoding="utf-8") as file:
            for baris in file:
                baris= baris.strip()
                parts= baris.split(",")
                if len(parts) != 3:
                    continue # Lewati baris yang tidak sesuai format
                kode,nama,stok_str = parts
                stok_int = int(stok_str)
                data_dict[kode] = {
                    "Nama": nama,
                    "Stok": stok_int,
                }
    except FileNotFoundError:
        print("File belum ada, akan dibuat saat simpan.")

    return data_dict

#=======================================================
#Fungsi 2 Menampilkan Data
#=======================================================
def tampilkan_data_barang(data_dict):

    #Membuka header tabel
    print("\n=== Daftar Barang ===")
    print(f"{'Kode':10} | {'Nama': <15} | {'Stok': >5}")
    print("-" * 33)

    for kode in sorted(data_dict.keys()):
        nama = data_dict[kode]["Nama"]
        stok = data_dict[kode]["Stok"]
        print(f"{kode:10} | {nama: <15} | {stok: >5}")

#=======================================================
#Fungsi 3 Mencari Data
#=======================================================
def cari_data(data_dict):
    #Mencari data maahsiswa berdasarkan NIM
    kode_cari = input("\nMasukkan Kode yang ingin dicari: ")
    if kode_cari in data_dict:
        nama = data_dict[kode_cari]["Nama"]
        stok = data_dict[kode_cari]["Stok"]

        print("\n=== Data Barang Ditemukan ===")
        print(f"Kode : {kode_cari}")
        print(f"Nama : {nama}")
        print(f"Stok : {stok}")
    else:
        print("\nData tidak ditemukan.")

#=======================================================
#Fungsi 4 Tambah Barang
#=======================================================
def tambah_barang(data_dict):

    kode = input("Masukkan kode barang: ")

    if kode in data_dict:
        print("Kode sudah digunakan.")
        return

    nama = input("Masukkan nama barang: ")

    try:
        stok = int(input("Masukkan stok awal: "))
    except ValueError:
        print("Stok harus angka.")
        return

    if stok < 0:
        print("Stok tidak boleh negatif.")
        return

    data_dict[kode] = {
        "Nama": nama,
        "Stok": stok
    }

    simpan_data(nama_file, data_dict) #Auto Simpan
    print("Barang berhasil ditambahkan & file diperbarui.")

#=======================================================
#Fungsi 5 Update Stok (AUTO SIMPAN)
#=======================================================
def update_stok(data_dict):

    #Cari NIM mahasiswa yang akan diupdate nilainya
    kode = input ("Masukkan kode barang yang akan diupdate stoknya: ")

    if kode not in data_dict:
        print("Kode tidak ditemukan, update dibatalkan.")
        return
    try:
        stok_baru = int(input("Masukkan stok baru: ").strip())
    except ValueError:
        print("Stok harus berupa angka, update dibatalkan.")
        return 

    if stok_baru < 0:
        print("Stok tidak boleh negatif.")
        return

    stok_lama = data_dict[kode]["Stok"]
    data_dict[kode]["Stok"] = stok_baru

    simpan_data(nama_file, data_dict) #Auto Simpan
    print(f"Update berhasil & file diperbarui. Stok {kode} berubah dari {stok_lama} menjadi {stok_baru}.")

#=======================================================
#Fungsi 6 Simpan File
#=======================================================
def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in sorted(data_dict.keys()):
            nama = data_dict[kode]["Nama"]
            stok = data_dict[kode]["Stok"]
            file.write(f"{kode},{nama},{stok}\n")

#=======================================================
#Fungsi 7 Menu
#=======================================================
def main():
    buka_data = baca_data_barang(nama_file)

    while True:
        print("\n=== Menu Utama ===")
        print("1. Tampilkan Semua Data") #fs no.2
        print("2. Cari Data Berdasarkan Kode") #fs no.3
        print("3. Tambah Barang") #fs no.4
        print("4. Update Stok Barang") #fs no.5
        print("5. Simpan Data ke File") #fs no.6
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == '1':
            tampilkan_data_barang(buka_data)
        elif pilihan == '2':
            cari_data(buka_data)
        elif pilihan == '3':
            tambah_barang(buka_data)
        elif pilihan == '4':
            update_stok(buka_data)
        elif pilihan == '5':
            simpan_data(nama_file, buka_data)
            print("Data berhasil disimpan.")
        elif pilihan == '0':
            print("Program selesai.")
            break

if __name__ == "__main__":
    main()

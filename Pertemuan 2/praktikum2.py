#=======================================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 1: Membuat Fungsi Load Data
#=======================================================

nama_file='data_mahasiswa.txt'

def baca_data_mahasiswa(nama_file):
    data_dict = {} #Inisialisasi data dictionary

    with open(nama_file,"r", encoding="utf-8") as file:
        for baris in file:
            baris= baris.strip()
            parts= baris.split(",")
            if len(parts) != 3:
                continue  # Lewati baris yang tidak sesuai format
            nim,nama,nilai_str = parts
            nilai_int = int(nilai_str)
            data_dict[nim] = {
                "Nama": nama,
                "Nilai": nilai_int,
            }
    return data_dict

#=======================================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 2 Membuat Fungsi Menampilkan Data
#=======================================================

def tampilkan_data_mahasiswa(data_dict):
    
    #Membuka header tabel
    print("\n=== Daftar Mahasiswa ===")
    print(f"{'NIM':10} | {'Nama': <12} | {'Nilai': >5}")
    print("-" * 33)

    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["Nama"]
        nilai = data_dict[nim]["Nilai"]
        print(f"{nim:10} | {nama: <12} | {nilai: >5}")

#=======================================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 3 Membuat Fungsi Mencari Data
#=======================================================

def cari_data(data_dict):
    #Mencari data mahasiswa berdasarkan NIM
    nim_cari = input("\nMasukkan NIM yang ingin dicari: ")
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["Nama"]
        nilai = data_dict[nim_cari]["Nilai"]

        print("\n=== Data Mahasiswa Ditemukan ===")
        print(f"NIM  : {nim_cari}")
        print(f"Nama : {nama}")
        print(f"Nilai: {nilai}")
    else:
        print("\nData tidak ditemukan.")

#=======================================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 4 Membuat fungsi Update Nilai
#=======================================================

def update_nilai(data_dict):

    #Cari NIM mahasiswa yang akan diupdate nilainya
    nim = input ("Masukkan NIM mahasiswa yang akan diupdate nilainya: ")

    if nim not in data_dict:
        print("NIM tidak ditemukan, update dibatalkan.")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru: ").strip())
    except ValueError:
        print("Nilai harus berupa angka, update dibatalkan.")
        return 

    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0-100, update dibatalkan.")
        return

    nilai_lama = data_dict[nim]["Nilai"]

    #Memasukkan nilai baru ke dalam dictionary
    data_dict[nim]["Nilai"] = nilai_baru

    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}.")

#=======================================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 5 Membuat Fungsi Menyimpan Perubahan Data ke File
#=======================================================

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["Nama"]
            nilai = data_dict[nim]["Nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

#=======================================================
#Praktikum 2: Konsep ADT dan File Handling (STUDI KASUS)
#Latihan 6 Membuat Menu
#=======================================================

def main():
    buka_data = baca_data_mahasiswa(nama_file)

    while True:
        print("\n=== Menu Utama ===")
        print("1. Tampilkan Semua Data") #fs no.2
        print("2. Cari Data Berdasarkan NIM") #fs no.3
        print("3. Update Nilai Mahasiswa") #fs no.4
        print("4. Simpan Data ke File") 
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == '1':
            tampilkan_data_mahasiswa(buka_data)
        elif pilihan == '2':
            cari_data(buka_data)
        elif pilihan == '3':
            update_nilai(buka_data)
        elif pilihan == '4':
            simpan_data(nama_file, buka_data)
            print("Data berhasil disimpan.")
        elif pilihan == '0':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
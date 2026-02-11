#===========================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 1A: Membaca seluruh isi file
#===========================================

#Membuka file dengan mode read ("r")

#Membuka file dalam satu string
with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    isi_file = file.read() #Membaca keseluruhan isi file dalam satu string
    print(isi_file)

print("--------------------------------------------")
print("=== Hasil Read ===")
print("Tipe Data: ", type(isi_file))
print("Jumlah Karakter", len(isi_file))
print("Jumlah Baris", isi_file.count("\n")+1)

#Membuka file per baris
print("=== Membaca File per Baris ===")
jumlah_baris = 0
with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip()
        print("Baris ke-", jumlah_baris)
        print("Isinya:", baris)
        
#=================================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 2A: Parsing baris menjadi kolom data
#=================================================

print("--------------------------------------------")

with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        print("NIM:",nim, "| Nama:",nama, "| Nilai:",nilai)

#=================================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 3A: Membaca File dan Menyimpan ke List
#=================================================

data_list = [] #List untuk menampung data mahasiswa

with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()

        #Simpan sebagai List"[nim,nama,nilai]"
        nim,nama,nilai = baris.split(",") #Parsing data berdasarkan karakter (,)
        data_list.append([nim,nama,int(nilai)])

    print("--------------------------------------------")

    print("=== Data Mahasiswa dalam List ===")
    print(data_list)

    print("=== Jumlah Record dalam List ===")
    print("Jumlah Record", len(data_list))

    print("=== Menampilkan Data Record Tertentu ===")
    print("Contoh Record Pertama: ", data_list[0])

#=================================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 4A: Menyimpan data ke dalam List
#=================================================

data_dict = {} #Buat variabel 
with open("data_mahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()

        #Simpan Sebagai list "[nim,nama,nilai]"
        nim,nama,nilai = baris.split(",") #Parsing data berdasarkan karakter (,)
        data_dict[nim] = {
            "Nama": nama,
            "Nilai": int(nilai),
        }

print("=== Data Mahasiswa dalam Dictionary ===")
print(data_dict)
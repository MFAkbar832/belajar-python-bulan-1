# MINGGU 3: HARI 6 - REFACTORING APLIKASI DAFTAR BELANJAAN (MODULAR)

# 1. FUNGSI MENAMPILKAN MENU
def tampilkan_menu():
    print("\n====================================")
    print("   APLIKASI DAFTAR BELANJAAN v2.0   ")
    print("====================================")
    print("1. Tambah Barang")
    print("2. Lihat Daftar Belanja")
    print("3. Hapus Barang")
    print("4. Keluar")
    print("====================================")

# 2. FUNGSI MENAMBAH BARANG
def tambah_barang(daftar):
    barang_baru = input("Masukkan nama barang yang ingin dibeli: ")
    daftar.append(barang_baru)
    print("Berhasil menambahkan '" + barang_baru + "' ke dalam daftar!")

# 3. FUNGSI MELIHAT DAFTAR BELANJA
def lihat_daftar(daftar):
    print("\n--- ISI DAFTAR BELANJA ANDA ---")
    if len(daftar) == 0:
        print("Daftar belanja masih kosong.")
    else:
        nomor = 1
        for item in daftar:
            print(str(nomor) + ". " + item)
            nomor = nomor + 1
        print("Total item: " + str(len(daftar)) + " barang")

# 4. FUNGSI MENGHAPUS BARANG
def hapus_barang(daftar):
    if len(daftar) == 0:
        print("Daftar belanja kosong, tidak ada yang bisa dihapus.")
        return  # Langsung keluar dari fungsi jika list kosong
        
    barang_hapus = input("Ketik nama barang yang ingin dihapus: ")
    if barang_hapus in daftar:
        daftar.remove(barang_hapus)
        print("'" + barang_hapus + "' berhasil dihapus dari daftar.")
    else:
        print("Error: Barang '" + barang_hapus + "' tidak ditemukan!")

# 5. FUNGSI UTAMA (PROGRAM ENGINE)
def main():
    # Variabel lokal di dalam main(), aman dari jebakan variabel global!
    daftar_belanja = []
    
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1/2/3/4): ")
        
        if pilihan == "1":
            tambah_barang(daftar_belanja)
        elif pilihan == "2":
            lihat_daftar(daftar_belanja)
        elif pilihan == "3":
            hapus_barang(daftar_belanja)
        elif pilihan == "4":
            print("Terima kasih telah menggunakan aplikasi ini. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid! Silakan masukkan angka 1 sampai 4.")

# MENJALANKAN PROGRAM UTAMA
main()
print("Lol")
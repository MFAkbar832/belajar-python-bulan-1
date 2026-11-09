# SOLO PROJECT BULAN 1: APLIKASI KASIR MINI (TAHAP 1)

# 1. FUNGSI MENAMPILKAN MENU
def tampilkan_menu():
    print("\n==========================================")
    print("         APLIKASI KASIR MINI POS          ")
    print("==========================================")
    print("1. Tambah Item ke Keranjang")
    print("2. Lihat Keranjang & Total Belanja")
    print("3. Proses Pembayaran")
    print("4. Keluar")
    print("==========================================")

# 2. FUNGSI MENAMBAH ITEM KE KERANJANG
def tambah_item(list_nama, list_harga, list_jumlah):
    print("\n--- TAMBAH BARANG ---")
    nama = input("Nama barang   : ")
    harga = int(input("Harga satuan  : Rp "))
    jumlah = int(input("Jumlah beli   : "))
    
    # Menyimpan data ke dalam 3 list paralel
    list_nama.append(nama)
    list_harga.append(harga)
    list_jumlah.append(jumlah)
    
    print("Sukses menambahkan " + str(jumlah) + "x " + nama + " ke keranjang!")

# 3. FUNGSI MELIHAT KERANJANG & MENGHITUNG TOTAL
def lihat_keranjang(list_nama, list_harga, list_jumlah):
    print("\n--- ISI KERANJANG BELANJA ---")
    
    if len(list_nama) == 0:
        print("Keranjang belanja masih kosong.")
        return 0  # Mengembalikan nilai total = 0
        
    total_keseluruhan = 0
    
    # Menggunakan range(len(...)) untuk mengakses index ke-i dari ketiga list secara bersamaan
    for i in range(len(list_nama)):
        subtotal = list_harga[i] * list_jumlah[i]
        total_keseluruhan = total_keseluruhan + subtotal
        
        nomor = i + 1
        print(str(nomor) + ". " + list_nama[i] + " (" + str(list_jumlah[i]) + " x Rp " + str(list_harga[i]) + ") = Rp " + str(subtotal))
        
    print("------------------------------------------")
    print("TOTAL BELANJA : Rp " + str(total_keseluruhan))
    return total_keseluruhan  # Mengembalikan angka total agar bisa dipakai di menu pembayaran besok!

# 4. PROGRAM UTAMA (MAIN ENGINE)
def main():
    nama_barang = []
    harga_barang = []
    jumlah_barang = []
    
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1/2/3/4): ")
        
        if pilihan == "1":
            tambah_item(nama_barang, harga_barang, jumlah_barang)
        elif pilihan == "2":
            lihat_keranjang(nama_barang, harga_barang, jumlah_barang)
        elif pilihan == "3":
            print("Fitur pembayaran akan kita buat di Hari 5!")
        elif pilihan == "4":
            print("Terima kasih telah menggunakan Aplikasi Kasir Mini!")
            break
        else:
            print("Pilihan tidak valid! Silakan masukkan angka 1-4.")

# JALANKAN PROGRAM
main()

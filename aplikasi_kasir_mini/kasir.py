# SOLO PROJECT BULAN 1: APLIKASI KASIR MINI (VERSI FINAL)

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
    
    list_nama.append(nama)
    list_harga.append(harga)
    list_jumlah.append(jumlah)
    
    print("Sukses menambahkan " + str(jumlah) + "x " + nama + " ke keranjang!")

# 3. FUNGSI MELIHAT KERANJANG & MENGHITUNG TOTAL
def lihat_keranjang(list_nama, list_harga, list_jumlah):
    print("\n--- ISI KERANJANG BELANJA ---")
    
    if len(list_nama) == 0:
        print("Keranjang belanja masih kosong.")
        return 0
        
    total_keseluruhan = 0
    for i in range(len(list_nama)):
        subtotal = list_harga[i] * list_jumlah[i]
        total_keseluruhan = total_keseluruhan + subtotal
        
        nomor = i + 1
        print(str(nomor) + ". " + list_nama[i] + " (" + str(list_jumlah[i]) + " x Rp " + str(list_harga[i]) + ") = Rp " + str(subtotal))
        
    print("------------------------------------------")
    print("TOTAL BELANJA : Rp " + str(total_keseluruhan))
    return total_keseluruhan

# 4. FUNGSI BARU: PROSES PEMBAYARAN & CETAK STRUK
def proses_pembayaran(list_nama, list_harga, list_jumlah):
    # Memanggil fungsi lihat_keranjang() untuk menampilkan rincian & mengambil total tagihan
    total_tagihan = lihat_keranjang(list_nama, list_harga, list_jumlah)
    
    # Jika keranjang kosong (total = 0), hentikan proses pembayaran
    if total_tagihan == 0:
        return
        
    print("\n--- PEMBAYARAN ---")
    # Menggunakan while True agar kasir bisa mengulang input jika uang pembeli kurang
    while True:
        uang_bayar = int(input("Masukkan jumlah uang tunai: Rp "))
        
        if uang_bayar < total_tagihan:
            kurang = total_tagihan - uang_bayar
            print("Uang tidak cukup! Kurang sebesar: Rp " + str(kurang))
        else:
            kembalian = uang_bayar - total_tagihan
            print("\n==========================================")
            print("           STRUK PEMBAYARAN LUNAS         ")
            print("==========================================")
            print("Total Tagihan : Rp " + str(total_tagihan))
            print("Uang Tunai    : Rp " + str(uang_bayar))
            print("Kembalian     : Rp " + str(kembalian))
            print("==========================================")
            print("    Terima Kasih Atas Kunjungan Anda!     ")
            print("==========================================")
            
            # Mengosongkan keranjang belanja untuk pelanggan berikutnya
            list_nama.clear()
            list_harga.clear()
            list_jumlah.clear()
            break  # Keluar dari loop pembayaran

# 5. PROGRAM UTAMA (MAIN ENGINE)
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
            # Memanggil fungsi pembayaran yang baru dibuat
            proses_pembayaran(nama_barang, harga_barang, jumlah_barang)
        elif pilihan == "4":
            print("Terima kasih telah menggunakan Aplikasi Kasir Mini!")
            break
        else:
            print("Pilihan tidak valid! Silakan masukkan angka 1-4.")

# JALANKAN PROGRAM
main()

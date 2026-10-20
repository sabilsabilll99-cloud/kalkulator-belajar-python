def kalkulator_belanja_otomatis():
    print("====================================")
    print("   🛒 KALKULATOR SAKU BELANJAAN 🛒  ")
    print("====================================")
    
    # DAFTAR BARANG YANG SUDAH DIBELI (Bisa kamu ubah/tambah sendiri angkanya)
    # Format data: (Nama Barang, Jumlah Beli, Harga Satuan)
    daftar_belanjaan = [
        ("Daging Ayam (kg)", 1, 35000),
        ("Telur Ayam (kg)", 2, 26000),
        ("Cabai Rawit (ons)", 3, 8000),
        ("Bawang Merah (kg)", 0.5, 32000),
        ("Bawang Putih (kg)", 0.5, 36000),
        ("Minyak Goreng (liter)", 2, 18000),
        ("Beras Premium (kg)", 5, 15000),
        ("Tempe Papan", 2, 600),
        ("Tahu Putih (bungkus)", 1, 5000),
        ("Sayur Kangkung (ikat)", 3, 2500)
    ]
    
    total_belanja = 0
    rangkuman_barang = []

    # Memproses daftar barang di atas secara otomatis menggunakan perulangan (loop)
    for nama_barang, jumlah, harga in daftar_belanjaan:
        # Menghitung subtotal per item (Jumlah x Harga)
        subtotal = jumlah * harga
        total_belanja += subtotal
        
        # Menyimpan hasil hitungan ke rangkuman
        rangkuman_barang.append((nama_barang, jumlah, harga, subtotal))

    # ================= CETAK NOTA / STRUK =================
    print("\n====================================")
    print("         STRUK BELANJAAN ANDA        ")
    print("====================================")
    
    for barang, qty, hrg, sub in rangkuman_barang:
        # Menampilkan jumlah barang dengan format jika ada desimal (misal 0.5 kg)
        qty_tampilan = int(qty) if qty.is_integer() else qty
        print(f"- {barang} ({qty_tampilan}x @ Rp {hrg:,.0f}): Rp {sub:,.0f}")
        
    print("------------------------------------")
    print(f"💰 TOTAL AKHIR : Rp {total_belanja:,.0f}")
    print("====================================")
    print("Semua barang berhasil dihitung otomatis! 🎉")

# Menjalankan aplikasi
if __name__ == "__main__":
    kalkulator_belanja_otomatis()

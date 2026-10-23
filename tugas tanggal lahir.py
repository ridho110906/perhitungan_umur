from datetime import datetime
import locale

def hitung_usia_rinci():
    """Meminta tanggal lahir, menghitung durasi hidup, dan menampilkan dalam hari, jam, menit, dan detik."""

    # Loop untuk memastikan input tanggal yang valid
    while True:
        try:
            # Meminta input tanggal lahir dari pengguna
            tanggal_lahir_str = input("Masukkan tanggal lahir Anda (format DD-MM-YYYY): ")
            
            # Mengubah string input menjadi objek datetime
            tanggal_lahir = datetime.strptime(tanggal_lahir_str, '%d-%m-%Y')
            break # Keluar dari loop jika input valid
        except ValueError:
            print("🚨 Format tanggal salah. Pastikan Anda menggunakan format DD-MM-YYYY. ")

    # Mendapatkan waktu saat ini
    waktu_saat_ini = datetime.now()

    # Menghitung selisih waktu (timedelta)
    selisih_waktu = waktu_saat_ini - tanggal_lahir

    # --- Konversi dan Perhitungan ---

    # Total detik dari selisih waktu
    total_detik = selisih_waktu.total_seconds()

    # Perhitungan Hari, Jam, Menit, Detik
    
    # Hari
    total_hari = selisih_waktu.days
    
    # Jam
    total_jam = int(total_detik // 3600)
    
    # Menit
    total_menit = int(total_detik // 60)
    
    # Detik
    # total_detik sudah dihitung di awal, tapi kita bulatkan
    total_detik_bulat = int(total_detik)


    # --- Tampilan Hasil ---
    
    print("\n" + "="*40)
    print("         HASIL PERHITUNGAN USIA ")
    print("="*40)
    
    print(f"Tanggal Lahir Anda :  {tanggal_lahir.strftime('%d %B %Y')}")
    print(f"Waktu Saat Ini     :  {waktu_saat_ini.strftime('%d %B %Y, %H:%M:%S')}")
    print("\n--- Durasi Hidup Anda ---")
    
    # Menampilkan dalam berbagai satuan
    print(f" Total Hari Anda Hidup  :   {total_hari:,} hari")
    print(f" Total Jam Anda Hidup   :   {total_jam:,} jam")
    print(f" Total Menit Anda Hidup :   {total_menit:,} menit")
    print(f" Total Detik Anda Hidup :   {total_detik_bulat:,} detik")
    
    print("="*40)

# Menjalankan fungsi utama
if __name__ == "__main__":
    hitung_usia_rinci()
import csv
import datetime
from barang import Barang
from transaksi import Transaksi



class Karyawan:
    def __init__(self, id, nama, umur, tanggal_masuk):
        self.id = id
        self.nama = nama
        self.umur = umur
        self.tanggal_masuk = tanggal_masuk
        self.mulai_bekerja = datetime.datetime.now()
        self.barang = set()

    def login(self):
        self.mulai_bekerja = datetime.datetime.now()

    def lihat_barang(self):
        existing_barang = set()
        try:
            with open("List_Barang.csv", mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    if len(row) >= 1:
                        id_barang = row[0]
                        existing_barang.add(id_barang)
        except FileNotFoundError:
            print("File List_Barang.csv tidak ditemukan.")
        return existing_barang

    def generate_id_barang(self):
        existing_ids = {barang.id_barang for barang in self.barang}
        index = 1
        while True:
            new_id = f"A-{index:04}"
            if new_id not in existing_ids:
                return new_id
            index += 1

    def tambah_barang(self):
        # Membaca ID maksimal terakhir dari file CSV
        max_id = 0
        try:
            with open("List_Barang.csv", mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    id_barang = row[0]
                    numeric_part = int(id_barang.split('-')[1])
                    max_id = max(max_id, numeric_part)
        except FileNotFoundError:
            pass

        new_id_numeric = max_id + 1
        new_id = f"A-{new_id_numeric:04}"

        nama_barang = input("Masukkan Nama Barang: ")
        harga = input("Masukkan Harga Jual Barang: ")
        stock = input("Masukkan Jumlah Barang: ")
        barang = Barang(new_id, nama_barang, harga, stock)
        self.barang.add(barang)
        print(f"Barang {barang.nama_barang} dengan ID {new_id} berhasil ditambahkan.")

        # Menyimpan data baru ke dalam file CSV
        with open("List_Barang.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([new_id, nama_barang, harga, stock])

    def akhiri_bekerja(self):
        session_duration = datetime.datetime.now() - self.mulai_bekerja
        print(f"Sesi Kerja Selesai. Total Waktu Anda Bekerja {session_duration}")
        return

    def tampilkan_menu_karyawan(self):
        while True:
            print("\nMenu Karyawan:")
            print("1. Lihat List Barang")
            print("2. Tambah Barang")
            print("3. Transaksi")
            print("4. Akhiri Shift Kerja")
            choice = input("Pilih tindakan (1/2/3/4): ")

            if choice == '1':
                existing_barang = self.lihat_barang()
                barang_obj = Barang('', '', '', '')  # Buat objek Barang kosong, karena __init__ membutuhkan argumen
                barang_obj.tampilkan_list_barang(existing_barang)
            elif choice == '2':
                self.tambah_barang()
            elif choice == '3':
                transaksi = Transaksi(self.id, datetime.datetime.now())  # Membuat objek Transaksi
                transaksi.tambah_transaksi(self.lihat_barang())  # Pass existing_barang ke objek Transaksi
                transaksi.proses_transaksi()  # Memanggil metode proses_transaksi dari objek Transaksi
            elif choice == '4':
                self.akhiri_bekerja()
                return
            else:
                print("Pilihan tidak valid.")
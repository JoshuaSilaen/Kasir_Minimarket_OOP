import csv
from barang import Barang

class Transaksi:
    def __init__(self, id_karyawan, waktu):
        self.id_karyawan = id_karyawan
        self.waktu = waktu
        self.transaksi = []

    def cari_barang(self, id_barang):
        with open('List_Barang.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['id_barang'] == id_barang:
                    return Barang(row['id_barang'], row['nama_barang'], row['harga'], row['stock'])
        return None

    def tambah_transaksi(self, existing_barang):
        while True:
            id_barang = input("Masukkan ID Barang yang Dibeli (0 untuk selesai): ")
            if id_barang == '0':
                break

            barang = self.cari_barang(id_barang)
            if barang is None:
                print("Barang tidak ditemukan.")
                continue

            jumlah_beli = int(input(f"Masukkan Jumlah Barang {barang.nama_barang} yang Dibeli: "))
            if int(barang.stock) < jumlah_beli:
                print("Stok barang tidak mencukupi.")
                continue

            self.transaksi.append((barang, jumlah_beli))
            print(f"{jumlah_beli} {barang.nama_barang} berhasil ditambahkan ke transaksi.")

    def proses_transaksi(self):
        total_harga = 0
        print("\nBon Belanja:")
        print(f"{'Nama Barang':<20}{'Jumlah':<10}{'Harga':<10}{'Total':<10}")
        print("=" * 50)
        for barang, jumlah in self.transaksi:
            harga_barang = int(barang.harga)
            total_barang = harga_barang * jumlah
            total_harga += total_barang
            print(f"{barang.nama_barang:<20}{jumlah:>10}Rp{harga_barang:>8}Rp{total_barang:>8}")

        print("=" * 50)
        print(f"Total Harga: Rp{total_harga:>36}")

        self.update_stok_barang()
        self.simpan_transaksi_ke_csv(total_harga)

    def update_stok_barang(self):
        with open('List_Barang.csv', 'r') as file:
            reader = csv.DictReader(file)
            data_barang = list(reader)

        for barang, jumlah in self.transaksi:
            for i in range(len(data_barang)):
                if data_barang[i]['id_barang'] == barang.id_barang:
                    data_barang[i]['stock'] = str(int(data_barang[i]['stock']) - jumlah)

        with open('List_Barang.csv', 'w', newline='') as file:
            fieldnames = ['id_barang', 'nama_barang', 'harga', 'stock']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_barang)

    def simpan_transaksi_ke_csv(self, total_harga):
        with open('Transaksi.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.id_karyawan, self.waktu, total_harga])

    def hitung_belanja(self, existing_barang):
        print("Mulai Transaksi (Masukkan 0 untuk selesai)")
        self.tambah_transaksi(existing_barang)
        if len(self.transaksi) > 0:
            self.proses_transaksi()

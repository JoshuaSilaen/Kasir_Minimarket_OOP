import csv
from karyawan import Karyawan

class Manajer:
    def __init__(self):
        self.karyawan = set()
        self.baca_dari_csv()

    def baca_dari_csv(self):
        try:
            with open("List_Karyawan.csv", mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    id, nama, umur, tanggal_masuk = row
                    karyawan = Karyawan(id, nama, umur, tanggal_masuk)
                    self.karyawan.add(karyawan)
        except FileNotFoundError:
            print("File List_Karyawan.csv tidak ditemukan.")

    def simpan_ke_csv(self):
        with open("List_Karyawan.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nama", "Umur", "Tanggal Masuk"])
            for karyawan in self.karyawan:
                writer.writerow([karyawan.id, karyawan.nama, karyawan.umur, karyawan.tanggal_masuk])

    def generate_id_otomatis(self):
        existing_ids = {karyawan.id for karyawan in self.karyawan}
        new_id = self.generate_new_id(existing_ids)
        return new_id

    def generate_new_id(self, existing_ids):
        index = 1
        while True:
            new_id = f"ID-{index:04}"
            if new_id not in existing_ids:
                return new_id
            index += 1

    def tambah_karyawan(self):
        new_id = self.generate_id_otomatis()
        nama = input("Masukkan nama karyawan: ")
        umur = input("Masukkan umur karyawan: ")
        tanggal_masuk = input("Masukkan tanggal masuk karyawan: ")
        karyawan = Karyawan(new_id, nama, umur, tanggal_masuk)
        self.karyawan.add(karyawan)
        print(f"Karyawan {karyawan.nama} dengan ID {new_id} berhasil ditambahkan.")
        self.simpan_ke_csv()

    def kurangi_karyawan(self, karyawan):
        karyawan_ditemukan = next((k for k in self.karyawan if k.id == karyawan.id), None)
        if karyawan_ditemukan:
            self.karyawan.remove(karyawan_ditemukan)
            print(f"Karyawan {karyawan_ditemukan.nama} berhasil dihapus.")
            self.simpan_ke_csv()
        else:
            print(f"Karyawan dengan ID {karyawan.id} tidak ditemukan.")
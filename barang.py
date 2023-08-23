import csv
class Barang:
    def __init__(self, id_barang, nama_barang, harga, stock):
        self.id_barang = id_barang
        self.nama_barang = nama_barang
        self.harga = harga
        self.stock = stock

    def tampilkan_list_barang(self, existing_barang):
        print("\nDaftar Barang:")
        print(f"{'ID':<10}{'Nama Barang':<20}{'Harga':<10}{'Stock':<10}")
        print("=" * 50)
        with open("List_Barang.csv", mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                id_barang, nama_barang, harga, stock = row
                if id_barang in existing_barang:
                    print(f"{id_barang:<10}{nama_barang:<20}Rp{harga:>8}  {stock:>5}")
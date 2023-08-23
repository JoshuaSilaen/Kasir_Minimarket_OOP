import csv
from karyawan import Karyawan
from manajer import Manajer

manager = Manajer()

print("\033[1m\033[4mMenu Utama\033[0m")
print("Masuk Sebagai:")
print("1. Manajer")
print("2. Karyawan")


def login_as_manager(manager):
    print("Anda berhasil masuk sebagai Manajemen.")
    while True:
        print("\nMenu Manajemen:")
        print("1. List Karyawan")
        print("2. Tambah Karyawan")
        print("3. Kurangi Karyawan")
        print("4. Simpan ke CSV")
        print("5. Kembali ke Menu Utama")
        choice = input("Pilih tindakan (1/2/3/4/5): ")

        if choice == '1':
            for karyawan in manager.karyawan:
                print(f"ID: {karyawan.id}, Nama: {karyawan.nama}, Umur: {karyawan.umur}, Tanggal Masuk: {karyawan.tanggal_masuk}")
        elif choice == '2':
            manager.tambah_karyawan()
        elif choice == '3':
            id = input("Masukkan ID karyawan yang akan dikurangi: ")
            karyawan = Karyawan(id, "", "", "")
            manager.kurangi_karyawan(karyawan)
        elif choice == '4':
            manager.simpan_ke_csv()
            print("Data karyawan berhasil disimpan ke List_Karyawan.csv.")
        elif choice == '5':
            print("Kembali ke Menu Utama.")
            break
        else:
            print("Pilihan tidak valid.")


def login_as_karyawan(karyawan_class):
    while True:
        print("Selamat Datang, Silahkan Masukkan ID Karyawan Anda:")
        masuk_id = input()

        with open('List_Karyawan.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            karyawan_found = False
            for row in reader:
                if row['ID'] == masuk_id:
                    print(f"Selamat Bekerja, {row['Nama']}!")
                    karyawan = karyawan_class(row['ID'], row['Nama'], row['Umur'], row['Tanggal Masuk'])
                    karyawan.login()  # Mulai jam kerja
                    karyawan.tampilkan_menu_karyawan()  # Tampilkan menu karyawan
                    karyawan_found = True
                    break

            if not karyawan_found:
                print("Maaf, Karyawan dengan ID tersebut tidak ada")
            else:
                break


while True:
    choice = input("Pilih opsi (1/2) atau ketik '0' untuk keluar: ")

    if choice == '1':
        login_as_manager(manager)
    elif choice == '2':
        login_as_karyawan(Karyawan)
    elif choice.lower() == '0':
        print("Terima Kasih! Sampai jumpa.")
        break
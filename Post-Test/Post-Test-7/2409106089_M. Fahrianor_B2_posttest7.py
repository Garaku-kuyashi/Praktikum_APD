import os

os.system('cls')

#ini adalah variabel global
user = "dr.fahri"
kode = "3336"
salah = 0
data_pack = {
    "dr.fahri": [
        {'nama pack': 'starter pack', 'harga': '16.000'},
        {'nama pack': 'monthly pack', 'harga': '79.000'}
    ]
}

#pada bagian ini akan diminta login dengan username "dr.fahri" dan kode "3336"
def login(user, kode):
    global salah  
    while salah < 3:
        os.system('cls')
        print("="*40)
        print("selamat datang di prts".center(40))
        print("="*40)
        username = input("Masukkan username: ")
        pasword = input("Masukkan kode: ")
        if user == username and kode == pasword:
            input(f"selamat anda berhasil masuk ke dalam prts, data anda dikenali sebagai {user}. Silahkan tekan enter untuk lanjut.")
            return True
        else:
            salah += 1
            print(f"Gagal {salah} kali")
            
    return False

#bagian ini akan menampilkan menu lihat pack
def lihat_pack(username):
    os.system('cls')
    print("="*40)
    print("Daftar pack".center(40))
    print("="*40)
    if username in data_pack:
        for i, pack in enumerate(data_pack[username], 1):
            print(i, pack)
    else:
        print("Tidak ada pack untuk user ini.")
    input("\nSilahkan tekan enter doktah")

#bagian ini akan menampilkan menu penambahan dan meminta untuk menambahkan pack baru 
#contoh pack baru yang bisa ditambahkan "nama pack: starter headhunting pack, harga: 450.000 "
def tambah_pack(username):
    os.system('cls')
    print("="*40)
    print("Tambah pack".center(40))
    print("="*40)
    pack_baru = input("Silahkan masukkan nama pack baru doktah: ")
    harga_pack = input("Silahkan masukkan harganya doktah: ")
    pack = {'nama pack': pack_baru, 'harga': harga_pack}    
    if username in data_pack:
        data_pack[username].append(pack)
    else:
        data_pack[username] = [pack]
    print("\nPack baru berhasil ditambah.")
    input("\nSilahkan tekan enter doktah")

#pada bagian ini akan diminta untuk memperbarui pack berupa nama pack dan harga pack
def edit_pack(username):
    os.system('cls')
    print("="*40)
    print("Perbarui pack".center(40))
    print("="*40)
    if username in data_pack:
        for i, pack in enumerate(data_pack[username], 1):
            print(i, pack)
        pilihan = int(input("Silahkan masukkan nomor pack yang mau diubah doktah: ")) - 1
        if 0 <= pilihan < len(data_pack[username]):
            nama_baru = input("Nama baru: ")
            harga_baru = input("Harga baru: ")
            data_pack[username][pilihan] = {'nama pack': nama_baru, 'harga': harga_baru}
            print("\nPack berhasil diubah.")
        else:
            print("Pilihan tidak ada doktah.")
    else:
        print("Tidak ada pack untuk user ini.")
    input("\nSilahkan tekan enter doktah")

#pada bagian ini akan diminta untuk memilih nomor pack berapa yang ingin di hapus
def hapus_pack(username):
    os.system('cls')
    print("="*40)
    print("Hapus pack".center(40))
    print("="*40)
    if username in data_pack:
        for i, pack in enumerate(data_pack[username], 1):
            print(i, pack)
        pilihan = int(input("Silahkan masukkan nomor pack yang mau dihapus doktah: ")) - 1
        if 0 <= pilihan < len(data_pack[username]):
            del data_pack[username][pilihan]
            print("\nPack berhasil dihapus.")
        else:
            print("Pilihan tidak ada doktah.")
    else:
        print("Tidak ada pack untuk user ini.")
    input("\nSilahkan tekan enter doktah")

#pada bagian ini adalah bagian menu yang bisa dipilih
def pilihan():
    if login(user, kode):
        while True:
            os.system('cls')
            print("="*40)
            print("Selamat datang doktah".center(40))
            print("="*40)
            print("1. Lihat pack")
            print("2. Tambah pack")
            print("3. Edit pack")
            print("4. Hapus pack")
            print("5. Log out")
            menu = input("\nMasukkan pilihan: ")

            if menu == "1":
                lihat_pack(user)
            elif menu == "2":
                tambah_pack(user)
            elif menu == "3":
                edit_pack(user)
            elif menu == "4":
                hapus_pack(user)
            elif menu == "5":
                os.system('cls')
                print("Anda telah log out dari prts.")
                break
            else:
                os.system('cls')
                print("="*40)
                print("Anomali".center(40))
                print("="*40)
                print("Tidak ada menu ini doktah, silahkan kembali.")
                input("\nSilahkan tekan enter doktah")
    else:
        print(f"Kamu gagal login sebanyak {salah} kali, maka kamu tidak bisa login lagi.")
pilihan()

import os  

os.system('cls')

#pada bagian ini digunakan username (dr.fahri) sebagai key nya dam nama pack danharga pack sebagai value nya
data_pack = {
    "dr.fahri":[
        {'nama pack': 'starter pack', 'harga': '16.000'},
        {'nama pack': 'monthly pack', 'harga': '79.000'}
    ]
}

user = "dr.fahri"
kode = "3336"
salah = 0

#pada bagian ini akan diminta login dengan username "dr.fahri" dan kode "3336"
while salah < 3:
    os.system('cls')
    print("="*40)
    print("selamat datang di prts".center(40))
    print("="*40)
    username = input("Masukkan username: ")
    pasword = input("Masukkan kode: ")
    if user == username and kode == pasword:
        input(f"selamat anda berhasil masuk ke dalam prts, data anda dikenali sebagai {user}. Silahkan tekan enter untuk lanjut.")
        break
    else:
        salah += 1
        print(f"Gagal {salah} kali")


if salah == 3:
    print(f"Kamu gagal login sebanyak {salah} kali, maka kamu tidak bisa login lagi.")
else: 
#ini ada;ah bagian menu yang bisa dipilih 
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


#bagian ini akan menampilkan menu lihat pack
        if menu == "1":
            os.system('cls')
            print("="*40)
            print("Daftar pack".center(40))
            print("="*40)
            if username in data_pack:
                for i, pack in enumerate(data_pack[username], 1):
                    print(i, pack)
            input("\nSilahkan tekan enter doktah")


#bagian ini akan menampilkan menu penambahan dan meminta untuk menambahkan pack baru 
#contoh pack baru yang bisa ditambahkan "nama pack: starter headhunting pack, harga: 450.000 "
        elif menu == "2":
            os.system('cls')
            print("="*40)
            print("Tambah pack".center(40))
            print("="*40)
            pack_baru = input("Silahkan masukkan nama pack baru doktah: ")
            harga_pack = input("Silahkan masukkan harganya doktah: ")
            if username in data_pack:
                data_pack[username].append({'nama pack': pack_baru, 'harga': harga_pack})
            print("\nPack baru berhasil ditambah.")
            input("\nSilahkan tekan enter doktah")

#pada bagian ini akan diminta untuk memperbarui pack berupa nama pack dan harga pack
        elif menu == "3":
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
                    input("\nsilahkan tekan enter doktah")
                else:
                    print("Pilihan tidak ada doktah.")
                    input("\nSilahkan tekan enter doktah")



#pada bagian ini akan diminta untuk memilih nomor pack berapa yang ingin di hapus
        elif menu == "4":
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
                    input("\nsilahkan tekan enter doktah")
                else:
                    print("Pilihan tidak ada doktah.")
                    input("\nSilahkan tekan enter doktah")


#pada bagian ini adalah bagian untuk log out
        elif menu == "5":
            os.system('cls')
            print("Anda telah log out dari prts.")
            break
        

#pada bagian ini adalah bagian ketika nomor yang dipilih tidak ada di menu  
        else:
            os.system('cls')
            print("="*40)
            print("Anomali".center(40))
            print("="*40)
            print("Tidak ada menu ini doktah, silahkan kembali.")
            input("\nSilahkan tekan enter doktah")

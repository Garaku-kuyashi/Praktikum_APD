import os

os.system('cls')

#ini adalah list data pack sementara
list_pack = [
{'nama pack' : 'starter pack' ,
 'harga' : '16.000'  
},

{'nama pack' : 'monthly pack',
 'harga' : '79.000'
}
]

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
        input(f"selamat anda berhasil masuk ke dalam prts data anda dikenali sebagai {user} silahkan tekan enter untuk lanjut")
        break
    else:
        salah += 1
        print(f"Gagal {salah} kali")

if salah == 3:
    print(f"kamu gagal login sebanyak {salah} kali maka kamu tidak bisa login lagi")
else:
#ini ada;ah bagian menu yang bisa dipilih   
    while True:
        os.system('cls')
        print("="*40)
        print("selamat datang doktah".center(40))
        print("="*40)
        print("1. Lihat pack")
        print("2. Tambah pack")
        print("3. Edit pack")
        print("4. Hapus pack")
        print("5. log out")
        menu = input("\nMasukkan pilihan: ")

        
#bagian ini akan menampilkan menu lihat pack 
        if menu == "1":
            os.system('cls')
            print("="*40)
            print("Daftar pack".center(40))
            print("="*40)
            for i, data in enumerate(list_pack,1):
                print(i, data)
            input("\n silahkan tekan enter doktah")

#bagian ini akan menampilkan menu penambahan dan meminta untuk menambahkan pack baru 
#contoh pack baru yang bisa ditambahkan "nama pack: starter headhunting pack, harga: 450.000 "
        elif menu == "2":
            os.system('cls')
            print("="*40)
            print("Tambah pack".center(40))
            print("="*40)
            pack_baru = input("silahkan masukkan pack baru doktah:")
            harga_pack = input("silahkan masukkan harganya doktah:")
            list_pack.append({
            "nama pack" : pack_baru,
            "harga" : harga_pack
        })
            print("\npack baru berhasil di tambah")
            input("\nsilahkan tekan enter doktah")

#pada bagian ini akan diminta untuk memperbarui pack berupa nama pack dan harga pack
        elif menu == "3":
            os.system('cls')
            print("="*40)
            print("Perbarui pack".center(40))
            print("="*40)
            for i, data in enumerate(list_pack,1):
                print(i,data)        
            pilihan = int(input("silahkan masukkan nomor list yang mau diubah doktah: "))-1
            if 0 <= pilihan < len(list_pack):
                nama = input("nama baru: ")
                harga =input("harga baru: ")
                list_pack[pilihan] = {"nama": nama, "harga": harga}
                print("\npack berhasil di ubah")
                input("\nsilahkan tekan enter doktah")
            else:
                print("pilihan tidak ada doktah")
                input("\nsilahkan tekan enter doktah")
                
#pada bagian ini akan diminta untuk memilih nomor pack berapa yang ingin di hapus
        elif menu == "4":
            os.system('cls')
            print("="*40)
            print("Hapus pack".center(40))
            print("="*40)

            for i, data in enumerate(list_pack,1):
                print(i,data)
                print()
            pilihan = int(input("silahkan masukkan nomor list yang mau diubah doktah: "))-1

            if 0 <= pilihan < len(list_pack):
                del_pack = list_pack.pop(pilihan)
                print("\npack berhasil dihapus")
                input("\nsilahkan tekan enter doktah")
            else:
                print("pilihan tidak ada doktah")
                input("\nsilahkan tekan enter doktah")

#pada bagian ini adalah bagian untuk log out
        elif menu == "5":
            os.system('cls')
            print("anda telah log out dari prts")
            break

#pada bagian ini adalah bagian ketika nomor yang dipilih tidak ada di menu        
        else:
            os.system('cls')
            print("="*40)
            print("anomali".center(40))
            print("="*40)
            print("tidak ada menu ini doktah silahkan kembali")
            input("\nsilahkan tekan enter doktah")





        

       
       
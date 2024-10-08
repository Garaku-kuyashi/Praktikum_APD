#silahkan masukkan apa saja yang ingin di isi
Nama_barang = str(input("Apa yang ingin anda beli: "))
Harga_barang = float(input("Silahkan masukkan harga barang: "))
Jumlah_barang = int(input("Berapa banyak anda ingin membeli: "))

#Diskon diisi sesuai dengan nim pembuat jadi disini nim saya adalah 89 maka diisi pada bagian diskon adalah 89
Diskon = float(input("Dimohon untuk memasukkan diskon berdasarkan dua digit terakhir nim: "))

#dikarenakan tidak bisa menuliskan diskon dalam persen seperti 89% maka saya membuatnya seperti ini
Diskon_dalam_persen = Diskon / 100 

#Bagian ini adalah bagian proses 
Harga_sebelum_diskon= Harga_barang * Jumlah_barang
Total_diskon = Harga_sebelum_diskon * Diskon_dalam_persen
Total_harga_setelah_diskon = Harga_sebelum_diskon - Total_diskon

#Bagian ini adalah modulus
Sisa_pembagian_diskon = Diskon%3

#Maka output dari keseluruhan adalah
print(f"""Anda membeli {Jumlah_barang} {Nama_barang} dengan harga satuan {Harga_barang},total sebelum diskon adalah {Harga_sebelum_diskon},total diskon adalah {Total_diskon}, dan total yang harus dibayar adalah {Total_harga_setelah_diskon}.
{Diskon} dibagi dengan 3 sisanya {Sisa_pembagian_diskon}""")


 
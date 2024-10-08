# list1 = ["a",
#          2,
#          True,
#          [1,2,3]]

# print(list1[-1][2])



# tas = ["buku", 32, True, 3.14, ["IF", 24]]

# print(tas)

# for i in tas:
#     print(i)

# print(len(tas))

# for i in range(len(tas)):
#     print(tas[i])



# matkul = ["kalkulus","fisdas","pti"]
# print(matkul)

# # matkul.append("sastra mesin")
# # print(matkul)
# # matkul.insert(1,"sastra mesin")

# matkul[1] = "fisika quantum"
# print(matkul)

# # del matkul [1]
# # print(matkul)

# buang = matkul.pop(1)
# print(matkul)

# print(f"variabel buang = {buang}")

# prodi = ["Informatika", "Sistem Informasi",
#           "Teknik Arsitektur", "Teknik Lingkungan", 
#           "Teknik Pertambangan", "Teknik Elektro",
#             "Teknik Industri", "Teknik Sipil", 
#             "TeknikGeologi", "Teknik Kimia"]

# print(prodi[::2], "\n",prodi)


# pryochar = ["hu tao","klee","xiangling"]
# hydrochar = ["furina","neuvilete","lapu-lapu"]

# party = pryochar + hydrochar
# print(pryochar,"\n")
# print(hydrochar,"\n")
# print(party)

# print(pryochar*3)

# barang = [["sepatu","kaus kaki","sarung"],
#           ["pulpen","pensil","laptop"]]
# print(barang[1][1])

# print(barang[-2][-1])
# print(barang)
# for i in barang:
#     for j in i:
#         print(j)


# nama = ("aldi","daffa","arisyi")
# print(nama)
# nama.append("rava")
# print(nama)


# barang1 = ("sepatu","kaus kaki","sarung"),
# barang2 =          ("pulpen","pensil","laptop")

# tuple2 = (barang1, barang2)

# print(tuple2)

# #mendeklarasikan tuple
# mahasiswa = (69, "Informatika", "2209106044", "Aldy septian ")
# #lalu kita unpacking
# absen, prodi, nim, nama, = mahasiswa
# #maka ketiga variabel tersebut akan berisi data dari tuple mahasiswa
# #menampilkan variabel
# print(absen)
# print(prodi)
# print(nim)
# print(nama)

mahasiswa = (69, "Informatika", "2209106044", "Aldy septian ")
print(mahasiswa)
mahasiswa = list(mahasiswa)
mahasiswa[2] = "2409106089"

mahasiswa = tuple(mahasiswa)
print(mahasiswa)



#pertemuan 6

# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

# daftar_buku = {}
# daftar_buku["novel 1"] = "senyum pertama di pagi hari airin"
# daftar_buku["1"]="matahari"
# print(daftar_buku)

# nama_dict = {
# "key1": "value",
# "key2": "value",
# "key3": "value"
# }

# daftar_buku = dict(buku1 = "harry potter", buku2 = "percy jakcson")
# # print(daftar_buku)

# print(daftar_buku["buku2"])
# print(daftar_buku.get("buku1"))

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# Nilai.update({"struktur data":"99"})
# Nilai.update({"struktur data":"100"})
# print(Nilai)


# for i in Nilai:
#     print(i)
#     print("")

# for i, j in Nilai.items():
#     print(f"nilai dari {i} itu valuenya adalah: {j}")


# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# print(Nilai)
# print()
# trashbin = Nilai.pop("Matematika")

# print(Nilai)
# print()
# print(type(trashbin))



# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# print(f"jumlah nilai adalah:",len(Nilai))

# daftar_nilai = Nilai.copy()
# print(daftar_nilai)

# key = "motor", "mobil", "sepeda"
# value = 2
# daftar = dict.fromkeys(key,value)
# print(daftar)

# Musik = {
# "The Chainsmoker" :["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
#     print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19},
# 111 : {"Nama" : "Abdul", "Umur" : 18, "hobi" : ["lari","jalan"]}
# }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     # for key_a, value_a in value.items():
#     #     print (key_a, " : ", value_a)
#     #     print("")
# print(mahasiswa[111]["hobi"])





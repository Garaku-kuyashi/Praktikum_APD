user = "m.fahrianor"
sandi = "89"
salah = 0

# Proses login
while salah < 3:
    username = input("Masukkan username: ")
    pasword = input("Masukkan password: ")
    if user == username and sandi == pasword:
        print("selamat ya kamu berhasil login")
        break
    else:
        salah += 1
        print(f"Gagal {salah} kali")

if salah == 3:
    print(f"kamu gagal login sebanyak {salah} kali maka kamu tidak bisa login lagi")
else:

    ulang= "ya"
    while ulang == "ya":       
        # Untuk berat badan karena dalam mg maka ditulis seperti ini, contoh (90000000)
        # Untuk tinggi badan karena ditulis dalam km maka ditulis seperti ini, contoh (0.0018)
        berat_badan_mg = float(input("masukkan berat badan anda dalam satuan mg:"))
        Tinggi_badan_km = float(input("masukkan tinggi badan anda dalam satuan km: "))
    
        #koversi
        Berat_Badan =  berat_badan_mg /  1000000
        Tinggi_Badan = Tinggi_badan_km * 1000

        BMI = Berat_Badan / (Tinggi_Badan ** 2)

        if BMI <= 18.5:
            Tipe ="berat badan anda Kurang(underweight)"
        elif BMI <= 24.9:
            Tipe = "berat badan anda normal"
        elif BMI <= 29.9:
            Tipe = "berat badan anda berlebih (overweight)"
        elif BMI >= 30:
            Tipe = "anda obesitas"

        print(f"""menurut perhitungan bmi hailnya adalah {BMI:.1f},jadi berdasarkan data menunjukkan bahwa{Tipe}""")

        ulang = input("ingin ulang ?")
    
        

        
        

        
    





        
        




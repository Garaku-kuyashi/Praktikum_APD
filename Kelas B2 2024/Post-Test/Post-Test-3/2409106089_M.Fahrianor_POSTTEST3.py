#untuk berat badan karena dalam mg maka di tulis seperti ini,contoh (90000000)
#untuk tinggi badan karena ditulis dalam kg maka di tulis seperti ini,comtoh (0.0018)
Berat_badan_mg = float(input("masukkan berat badan anda dalam satuan mg: "))
Tinggi_badan_km = float(input("masukkan tinggi badan anda dalam satuan km: "))

#menkonversi hasil inputan 
Berat_Badan =  Berat_badan_mg /  1000000
Tinggi_Badan = Tinggi_badan_km * 1000

#menghitung hasil konversi (pada bagian tinggi badan ** 2 bisa pula ditulis seperti ini tinggi_badan * tinggi_badan)
BMI = Berat_Badan / (Tinggi_Badan ** 2)


if BMI <= 18.5:
    Tipe ="berat badan anda Kurang(underweight)"
elif BMI <= 24.9:
    Tipe = "berat badan anda normal"
elif BMI <= 29.9:
    Tipe = "berat badan anda berlebih (overweight)"
elif BMI >= 30:
    Tipe = "anda obesitas"

print(f"""menurut perhitungan bmi hailnya adalah {BMI:.1f},jadi berdasarkan data menunjukkan bahwa 
{Tipe}""")
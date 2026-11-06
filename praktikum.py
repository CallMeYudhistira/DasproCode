"""
Nama: Yudhistira
NIM: 2603120
Kelas: 1C
Materi: Function dan Prosedure
"""

"""
Latihan 1
"""

# 1. Fibonacci

def fibonacci(n, a = 0, b = 1):
    if n == 0:
        print(a)
        return
    else:
        print(a)
        return fibonacci(n-1,b,a+b)

fibonacci(7)

# 0, 1, 1, 2, 3, 5, 8, 13

# 2. Hitung Volume Tabung
def volume_tabung(jari_jari, tinggi):
    return 3.14 * pow(jari_jari, 2) * tinggi

print(volume_tabung(10, 10))

# 3. Menghitung Nilai Total dan Rata-Rata
input_angka = []

def nilai_total(*angka):
    total = sum(angka)
    return total

def nilai_rata_rata(*angka):
    total = sum(angka)
    jumlah_angka = len(angka)
    rata_rata = total / jumlah_angka
    return rata_rata

jumlah_angka = int(input('Masukan jumlah angka: '))

for i in range(jumlah_angka):
    input_angka.append(int(input(f"Masukan nilai dari angka ke {i+1} : ")))
    
print(f"Total : {nilai_total(*input_angka)}")
print(f"Rata-rata : {nilai_rata_rata(*input_angka)}")


"""
Latihan 2
"""

# Membuat Login

username = "Daspro2023"
password = "Latihan"
sisa_kesempatan = 3

def kesempatan(password):
    if password == "Latihan":
        return True
    else:
        return False

print("Login SMAN 2 Harapan")

while sisa_kesempatan > 0:
    username_input = input("\nMasukan username: ")
    password_input = kesempatan(input("Masukan password: "))

    if password_input:
        print("Login Berhasil!")
        break
    else:
        sisa_kesempatan -= 1
        if sisa_kesempatan == 0:
            print("Kesempatan login telah habis!")
        else:
            print(f"Password salah! Sisa kesempatan Anda: {sisa_kesempatan}")    

"""
Latihan 3
"""

# Menghitung Selisih Waktu

def hitung_selisih_waktu(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai):
    total_detik_mulai = (jam_mulai * 3600) + (menit_mulai * 60) + detik_mulai
    total_detik_selesai = (jam_selesai * 3600) + (menit_selesai * 60) + detik_selesai

    selisih_detik = total_detik_selesai - total_detik_mulai

    jam = selisih_detik // 3600
    sisa_detik = selisih_detik % 3600
    menit = sisa_detik // 60
    detik = sisa_detik % 60

    return f"{jam} jam - {menit} menit - {detik} detik"

print("Input Mulai:")
jam_mulai = int(input("Masukan jam mulai: "))
menit_mulai = int(input("Masukan menit mulai: "))
detik_mulai = int(input("Masukan detik mulai: "))

print("\nInput Selesai:")
jam_selesai = int(input("Masukan jam selesai: "))
menit_selesai = int(input("Masukan menit selesai: "))
detik_selesai = int(input("Masukan detik selesai: "))

hasil = hitung_selisih_waktu(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai)
print(f"\nOutput: {hasil}")
"""
Nama: Yudhistira
NIM: 2603120
Kelas: 1C
Materi: Function dan Prosedure
"""

loop = True
while (loop):
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

    # 2. Hitung Volume Tabung
    def volume_tabung(jari_jari, tinggi):
        return 3.14 * pow(jari_jari, 2) * tinggi

    # 3. Menghitung Nilai Total dan Rata-Rata
    def nilai_total(*angka):
        total = sum(angka)
        return total

    def nilai_rata_rata(*angka):
        total = sum(angka)
        jumlah_angka = len(angka)
        rata_rata = total / jumlah_angka
        return rata_rata

    """
    Latihan 2
    """

    # Membuat Login
    def kesempatan(password):
        if password == "Latihan":
            return True
        else:
            return False

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

    print("1. Fibonacci")
    print("2. Hitung Volume Tabung")
    print("3. Menghitung Nilai Total dan Rata-rata")
    print("4. Login")
    print("5. Hitung Selisih Waktu")

    pilihan = int(input("\nMasukan pilihan: "))

    if pilihan == 1:
        n = int(input("Masukan nilai suku fibonacci: "))
        fibonacci(n)
    elif pilihan == 2:
        jari_jari = int(input("Masukan nilai jari-jari: "))
        tinggi = int(input("Masukan nilai tinggi: "))
        print(volume_tabung(jari_jari, tinggi))
    elif pilihan == 3:
        input_angka = []

        jumlah_angka = int(input('Masukan jumlah angka: '))

        for i in range(jumlah_angka):
            input_angka.append(int(input(f"Masukan nilai dari angka ke {i+1} : ")))
        
        print(f"Total : {nilai_total(*input_angka)}")
        print(f"Rata-rata : {nilai_rata_rata(*input_angka)}")
    elif pilihan == 4:
        username = "Daspro2023"
        password = "Latihan"
        sisa_kesempatan = 3
            
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
    elif pilihan == 5:
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
    else:
        print("Pilihan tidak valid.")

    loop = True if str(input("Ingin mengulang? (y/n): ")).lower() == 'y' else False
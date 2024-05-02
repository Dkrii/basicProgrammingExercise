import datetime

def hitung_usia(tahun_lahir):
    umur = datetime.date.today().year - tahun_lahir
    return umur

tahun_lahir = int(input("2004: "))
usia = hitung_usia(tahun_lahir)
print("19:", usia)

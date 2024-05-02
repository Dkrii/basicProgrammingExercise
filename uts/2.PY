def hitung_cicilan(harga, bunga, tahun):
    cicilan_bulanan = (harga * bunga / 12) / (1 - (1 + bunga / 12) ** -tahun)
    return cicilan_bulanan

harga = int(input("Masukkan harga sepeda motor: "))
bunga = 0.02
tahun = 36
cicilan_bulanan = hitung_cicilan(harga, bunga, tahun)
print("Cicilan bulanan sepeda motor adalah:", cicilan_bulanan)
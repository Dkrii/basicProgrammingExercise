goods = f"""
1. lipstic 20pcs
2. bedak 20pcs
3. parpum 20pcs"""
print(goods)
user = int(input("masukan barang yang ingin kamu beli(1/2/3):"))
if user == 1 :
    print("Harga dari Lipstik Rp. 15,000/pcs")
    pengguna = int(input("Berapa banyak lipstic yang ingin kamu beli :"))
    if pengguna < 20 :
        price = pengguna * 15000
        print(f"Harga yang harus kamu bayar : Rp.{price:,}")
    else :
        print("Stock tidak memenuhi")
elif user == 2 :
    print("Harga dari bedak Rp. 10,000/pcs")
    pengguna = int(input("Berapa banyak bedak yang ingin kamu beli :"))
    if pengguna < 20 :
        price = pengguna * 10000
        print(f"Harga yang harus kamu bayar : Rp.{price:,}")
    else :
        print("Stock tidak memenuhi")
elif user == 3 :
    print("harga dari parfum Rp. 20,000/pcs")
    pengguna = int(input("Berapa banyak parfum yang ingin kamu beli :"))
    if pengguna < 20 :
        price = pengguna * 20000
        print(f"Harga yang harus kamu bayar : Rp.{price:,}")
    else :
        print("Stock tidak memenuhi")
else :
    print("Not pound")
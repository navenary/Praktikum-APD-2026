print("==Harga Belanja==")
barang_1 = 15000
barang_2 = 25000
barang_3 = 10000
barang_4 = 5500
barang_5 = 5000
barang_6 = 20000

print("barang_1:",barang_1)
print("barang_2:",barang_2)
print("barang_3:",barang_3)
print("barang_4:",barang_4)
print("barang_5:",barang_5)
print("barang_6:",barang_6)

print()

print("==Perhitungan Total Dan Pajak==")
total_belanja = barang_1 + barang_2 + barang_3 + barang_4 + barang_5 + barang_6
print("Total Belanja:",total_belanja)

pajak = total_belanja * 15 / 100
print ("Pajak(15%):",pajak)

total_bayar = total_belanja + pajak
print ("Total Bayar:",total_bayar)

print() 

print("==Hasil Belanja Andi==")
print("Total Yang Harus Dibayar:",total_bayar)

print() 

print ("==Perhitungan Rata-Rata==")
rata_rata = total_bayar / len([barang_1, barang_2, barang_3, barang_4, barang_5, barang_6])
print("Rata-Rata:",rata_rata)

print() 

print("==NIM Dan Bolean==")
nim = 14
bolean = nim < rata_rata
print("NIM:",nim)
print ("Bolean:",bolean)

print()

print("==List Barang==")
barang = [barang_1, barang_2, barang_3, barang_4, barang_5, barang_6]
print("List Barang:",barang)

print() 

print("==Konversi Mata Uang==")
kurs_sgd = 13948.89
kurs_peso = 283.75
sgd = total_bayar / kurs_sgd
peso = total_bayar /kurs_peso
print("SGD:",sgd)
print("Peso:",peso)

print() 

print("==Slicing List Barang==")
print("Menampilkan Barang 1, Barang 3, dan Barang 5")
print("Menampilkan Barang Menggunakan Slicing:",barang[0:5:2])

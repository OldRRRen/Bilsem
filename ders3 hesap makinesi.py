print ("""Hesap Makinesie Hoşgeldiniz yapmak istediğiniz işlemi seçiniz
1 toplama
2 çıkarma
3 bölme 
4 çarpma 
5 üst al 
6 kalan bul 
7 çıkış""")

secim = input("bir seçim yapınız")
sayi1 = int(input("sayı1"))
sayi2 = int(input("sayı2"))
if secim=="1":
    print(sayi1 + sayi2)
elif secim=="2":
    print(sayi1 - sayi2)
elif secim=="3":
    print(sayi1 / sayi2)
elif secim=="4":
    print(sayi1 * sayi2)
elif secim=="5":
    print(sayi1 ** sayi2)
elif secim=="6":
    print(sayi1 % sayi2)


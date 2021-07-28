
deger = int(input("Bir değer giriniz. "))

asalSayilar = []

if deger <= 2:
    print(str(deger) + " değerine kadar asal sayı yoktur.")
elif deger == 3:
    asalSayilar.insert(0,2)
    print(str(deger) + " değerine kadar olan asal sayılar:")
    print(asalSayilar)
else:
    asalSayilar.insert(0,2)
    asalSayilar.insert(1,3)
    index = 2
    for x in range(4, deger):
        for a in range(2,x):
            if x % a == 0:
                b = 1
                break
            else:
                b = 0
        if b == 0:
            asalSayilar.insert(index, x)
            index = index + 1
    print(str(deger) + " değerine kadar olan asal sayılar:")
    print(asalSayilar)

b = 0

if deger < 2:
    print(str(deger) + " değeri asal değildir.")
elif deger == 2:
    print(str(deger) + " değeri asal bir sayıdır.")
elif deger == 3:
    print(str(deger) + " değeri asal bir sayıdır.")
else:
    for x in range(2,deger):
        if deger % x == 0:
            b = 1
            break
        else:
            b = 0
    if b == 1:
        print(str(deger) + " değeri asal değildir.")
    else:
        print(str(deger) + " değeri asal bir sayıdır.")
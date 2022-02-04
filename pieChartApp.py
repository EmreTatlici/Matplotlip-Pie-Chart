import matplotlib.pyplot as plt

# meyvelerin olsun, kullanici meyve alsin, ve buna bagli olarak satilan meyve oranlarini pasta grafigi uzerinde gosteriniz.

alinan_meyveler = [0,0,0,0,0]

meyveler = ['elma','armut','muz','cilek','seftali']


def meyveAl(meyveAdi):
    for meyve in meyveler:
        if meyveAdi == meyve:
            indeks = meyveler.index(meyveAdi)
            alinan_meyveler[indeks] += 1


while True:
    islem = input('1- meyve satin al\n2- pie chart goster\n3- cikis yap\n')

    if islem == '1':
        meyveAdi = input('meyve adi gir: ')
        meyveAl(meyveAdi)


    elif islem == '2':
        pieChart = plt.pie(alinan_meyveler, labels= meyveler,autopct='%1.1f%%')
        # explode = myexplode
        plt.legend()
        plt.show()

    elif islem == '3':
        break
    else:
        print('hatali tuslama!!')



































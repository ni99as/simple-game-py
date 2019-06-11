import random
import time

def intronya():
    print('Kamu sedang berada dalam sarang naga. Didepanmu ada dua gua.')
    print('Di masing - masing gua dihuni oleh naga.')
    print('Di salah satu gua terdapat seekor naga baik hati, dia akan membagikan harta karunnya kepadamu.')
    print('Sedangkan di gua satu lagi terdapat naga jahat yang akan memangsamu apabila melihatmu.')
    print()

def pilihGuanya():
    gua = ''
    while gua != '1' and gua != '2':
        print('Gua mana yang kamu ingin masuk kedalamnya? (1 atau 2)')
        gua = input()
        return gua

def cekGua(guaTerpilih):
    print('Kamu memasuki gua...')
    time.sleep(2)
    print('Gua nya gelap dan menyeramkan...')
    time.sleep(2)
    print('Seekor naga besar melompat kearahmu membuka rahangnya dan...')
    print()
    time.sleep(2)

    guaBaik = random.randint(1, 2)

    if guaTerpilih == str(guaBaik):
        print('Ini harta karun untukmu!')
    else:
        print('Kamu ditelan dalam sekali gigit!')

mainLagi = 'Iya'
while mainLagi == 'Iya' or mainLagi == 'y':

    intronya()

    nomorGua = pilihGuanya()

    cekGua(nomorGua)

    print('Kamu mau main lagi? (Iya atau Tidak)')
    mainLagi = input()
'''P'Chang in another dimension'''

def slowwwww(menu, dish, queue, premium, time=0):
    '''I HAVE PREMIUM, SO QUICKLY PLEASE!!!'''
    suki = (menu == "Suki Haeng Tha le Khai dao Phet Noi Sai Sauce Yer Yer") * 1049
    basil = (menu == "Kaphrao Mu Krop Pri Sret Mai Phrik Khai dao Khai daeng Keop Suk") * 346
    vegan = (menu == "Mu Sap Phat NammanHoi Khai dao Vegan") * 3
    soup, spagh = (menu == "Kaengsom Saeb Saeb") * 124, (menu == "Sapa Ket Ti Kha Bo Na Ra") * 1832
    other = suki != 0 or basil != 0 or vegan != 0 or soup != 0 or spagh != 0
    time += (suki + basil + vegan + soup + spagh) * dish + queue * premium * other
    day, hour, mnt, sec = time // 86400, time % 86400 // 3600, time % 86400 % 3600 // 60, time % 60
    print("%02d days %02d hours %02d mins %02d secs." %(day, hour, mnt, sec)\
        + "\nYou've starved to death." * (time > 259200))
slowwwww(input(), float(input()), float(input()) * 1800, input() == "No")

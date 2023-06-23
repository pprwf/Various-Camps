'''Sleep Enough?'''

def sleep(slhr, slmn, wkhr, wkmn):
    '''Sleep Enough?'''
    slp, wake = slhr * 60 + slmn, wkhr * 60 + wkmn
    if slp > wake:
        slp -= 1440
    if wake - slp >= 450:
        print("Sleep enough!")
    else:
        wake += 450 - (wake - slp)
        print("P'Guy have to wake up at %02d:%02d" %(wake // 60 % 24, wake % 60))
sleep(int(input()), int(input()), int(input()), int(input()))

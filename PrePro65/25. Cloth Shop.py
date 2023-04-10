'''Erza Scarlet'''

def erza():
    '''clothes'''
    occupation = input()
    price = 12800
    if occupation == "Magician":
        guild = input()
        amount = int(input())
        if guild == "Fairy Tail":
            price -= 2560
            print("Total %d Jewel" %(price * amount))
        elif guild == "Sabertooth" and amount > 5:
            price -= 1920
            print("Total %d Jewel" %(price * amount))
        elif guild == "Lamia Scale" and amount >= 3:
            price -= 1280
            print("Total %d Jewel" %(price * amount))
        elif guild == "Blue Pegasus" and amount > 10:
            price -= 640
            print("Total %d Jewel" %(price * amount))
        else:
            print("Total %d Jewel" %(price * amount))
    else:
        amount = int(input())
        print("Total %d Jewel" %(price * amount))
erza()

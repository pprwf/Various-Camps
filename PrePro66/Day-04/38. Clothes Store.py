'''ร้านขายเสื้อของจอมเวทย์'''

def cloth(job, price=12800):
    '''ร้านขายเสื้อของจอมเวทย์'''
    guild = input() if job == "Magician" else None
    amount = int(input())
    if guild == "Fairy Tail":
        price -= 2560
    elif guild == "Sabertooth" and amount > 5:
        price -= 1920
    elif guild == "Lamia Scale" and amount >= 3:
        price -= 1280
    elif guild == "Blue Pegasus" and amount > 10:
        price -= 640
    print("Total %d Jewel" %(price * amount))
cloth(input())

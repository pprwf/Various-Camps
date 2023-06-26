'''ค่าไฟนั้นแพง'''

def electricity(televi, microwave, hairdryer, bulb, fridge):
    '''ค่าไฟนั้นแพง'''
    print("TV %d Watt 1 ea for 3 hours\n%.2f unit." %(televi, televi * 3 / 1000 * 30))
    print("Microwave %d Watt 1 ea for 1 hours\n%.2f unit." %(microwave, microwave / 1000 * 30))
    print("Hair dryer %d Watt 1 ea for 0.5 hours\n%.2f unit." %(hairdryer, hairdryer / 2000 * 30))
    print("light bulb %d Watt 4 ea for 5 hours\n%.2f unit." %(bulb, bulb / 200 * 30 * 4))
    print("Refrigerator %d Watt 1 ea for 24 hours\n%.2f unit." %(fridge, fridge * 24 / 1000 * 30))
electricity(int(input()), int(input()), int(input()), int(input()), int(input()))

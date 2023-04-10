'''ค่าไฟ'''
def unit(watt, hour):
    '''Equation'''
    return (watt * hour) / 1000 * 30

def elec():
    '''การไฟฟ้า'''
    tele = int(input())
    micro = int(input())
    hair = int(input())
    bulb = int(input())
    frige = int(input())
    print("TV %d Watt 1 ea for 3 hours\n%.2f unit." %(tele, unit(tele, 3)))
    print("Microwave %d Watt 1 ea for 1 hours\n%.2f unit." %(micro, (unit(micro, 1))))
    print("Hair dryer %d Watt 1 ea for 0.5 hours\n%.2f unit." %(hair, unit(hair, 0.5)))
    print("light bulb %d Watt 4 ea for 5 hours\n%.2f unit." %(bulb, unit(bulb * 4, 5)))
    print("Refrigerator %d Watt 1 ea for 24 hours\n%.2f unit." %(frige, unit(frige, 24)))
elec()

'''หารร่วมมาก'''

def gcd(numx, numy):
    '''Greatest Common Division'''
    return numx if numy == 0 else gcd(numy, numx % numy)

def main(numx, numy):
    '''Main Function'''
    print("Number is", gcd(numx, numy))
main(int(input()), int(input()))

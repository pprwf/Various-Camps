'''Velocity'''

def main():
    '''ระบบ'''
    distance = float(input())
    time = int(input())
    print("อัตราเร็วเท่ากับ : %.3f เมตรต่อวินาที" \
    %((distance*1852)/(time*0.001)))
main()

'''ตัวเลขกำลังแพร่กระจาย'''

def main(num):
    '''ตัวเลขกำลังแพร่กระจาย'''
    print(num + int(str(num) + str(num)) + int(str(num) + str(num) + str(num)))
main(int(input()))

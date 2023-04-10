'''ตารางสูตรคูณ'''

def cute():
    '''เพราะเธออะน่ารักจนเกินต้าน'''
    num = int(input())
    mnum = int(input())
    for i in range(2, num + 1):
        print("-----")
        for j in range(1, mnum + 1):
            print("%d x %d = %d" %(i, j, i * j))
        if i == num:
            print("-----")
            break
cute()

'''txt'''

def txtsrt(txt, txt2, txt3):
    '''เรียงข้อความ ยามเธออ่านไม่ตอบ'''
    if len(txt) > len(txt2):
        txt, txt2 = txt2, txt
    if len(txt) > len(txt3):
        txt, txt3 = txt3, txt
    if len(txt2) > len(txt3):
        txt2, txt3 = txt3, txt2
    print("%s\n%s\n%s" %(txt, txt2, txt3))
txtsrt(input().capitalize(), input().capitalize(), input().capitalize())

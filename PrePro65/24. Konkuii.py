'''ใครออกโจทย์อะ'''

def lovely():
    '''พี่อย่าหลายใจดิ ผมไม่ชอบเลยคนแบบนี้ แย่มากๆ'''
    prefer1 = input()
    prefer2 = input()
    if prefer1 == "Calm" or prefer2 == "Calm":
        if prefer1 == "Empathetic" or prefer2 == "Empathetic":
            print("Ice")
        elif prefer1 == "Courageous" or prefer2 == "Courageous":
            print("Dream")
    elif prefer1 == "Reliable" or prefer2 == "Reliable":
        if prefer1 == "Courageous" or prefer2 == "Courageous":
            print("Fern")
        elif prefer1 == "Optimistic" or prefer2 == "Optimistic":
            print("Prae")
    elif prefer1 == "Cheerful" or prefer2 == "Cheerful":
        if prefer1 == "Optimistic" or prefer2 == "Optimistic":
            print("Bam")
        elif prefer1 == "Creative" or prefer2 == "Creative":
            print("Mild")
    elif prefer1 == "Attractive" or prefer2 == "Attractive":
        if prefer1 == "Creative" or prefer2 == "Creative":
            print("Tangmo")
        elif prefer1 == "Empathetic" or prefer2 == "Empathetic":
            print("Aom")
lovely()

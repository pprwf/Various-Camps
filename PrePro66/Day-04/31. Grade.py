'''คำนวนเกรดให้พี่ศิลาหน่อยได้ไหม'''

def grade(score):
    '''คำนวนเกรดให้พี่ศิลาหน่อยได้ไหม'''
    if 80 <= score <= 100:
        print("Grade : A\nYahoo!")
    elif 75 <= score < 80:
        print("Grade : B+\nYahoo!")
    elif 70 <= score < 75:
        print("Grade : B\nYahoo!")
    elif 65 <= score < 70:
        print("Grade : C+\nYahoo!")
    elif 60 <= score < 65:
        print("Grade : C\nTry again!")
    elif 50 <= score < 60:
        print("Grade : D+\nTry again!")
    elif 0 <= score < 50:
        print("Grade : F\nSo sad!")
    else:
        print("Grade : N/A\nI'm confused")
grade(float(input()))

'''Make it ez'''
# ติดปัญหาแค่การเรียงชื่อคน

def not_easy(num):
    '''liar'''
    if num > 50:
        num = 50
    elif num < 1:
        num = 1
    data = []
    job = []
    for _ in range(num):
        info = input().split(" ")
        if info[2].upper() in job:
            pass
        else:
            job.append(info[2].upper())
        data.append(info[2].upper())
        data.append(info[1])
        data.append(info[0])
    job.sort()
    time = 1
    for i in job:
        print("OCCUPATION :", i)
        for j in range(len(data)):
            if data[j] == i:
                print(str(time) + ". %s, %s" %(data[j + 1], data[j + 2]))
                time += 1
        time = 1
not_easy(int(input()))

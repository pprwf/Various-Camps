'''วิ่งเก็บ'''

def run(dist):
    '''kankyrook'''
    start = float(dist[0])
    for i in range(len(dist) - 1):
        if float(dist[i]) >= float(dist[i + 1]):
            start += float(dist[i]) - float(dist[i + 1])
        else:
            start += float(dist[i + 1]) - float(dist[i])
    print("%.2f" %start)
run(input().split())

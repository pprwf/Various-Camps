'''Concurrent Timeline'''

def main(sec):
    '''Concurrent Timeline'''
    print("%02d:%02d:%02d:%02d" %(sec // 86400, sec % 86400 // 3600,
                                  sec % 86400 % 3600 // 60, sec % 86400 % 3600 % 60))
main(int(input()))

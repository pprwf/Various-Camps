'''Toy Factory'''

def factory():
    '''toy'''
    first = input().replace("1", " ^----^").replace("2", "( 0--0 )")
    first = first.replace("3", "<------>").replace("4", "(------)").replace("5", " u----u")
    second = input().replace("1", " ^----^").replace("2", "( 0--0 )")
    second = second.replace("3", "<------>").replace("4", "(------)").replace("5", " u----u")
    third = input().replace("1", " ^----^").replace("2", "( 0--0 )")
    third = third.replace("3", "<------>").replace("4", "(------)").replace("5", " u----u")
    fourth = input().replace("1", " ^----^").replace("2", "( 0--0 )")
    fourth = fourth.replace("3", "<------>").replace("4", "(------)").replace("5", " u----u")
    fifth = input().replace("1", " ^----^").replace("2", "( 0--0 )")
    fifth = fifth.replace("3", "<------>").replace("4", "(------)").replace("5", " u----u")
    print("%s\n%s\n%s\n%s\n%s" %(first, second, third, fourth, fifth))
factory()

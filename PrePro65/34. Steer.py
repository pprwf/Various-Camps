'''Steer'''

def main():
    '''main'''
    fishes = input()
    crew = int(input())
    fish = "<^))))><"
    if fishes.count("<^))))><") > (fish * crew).count("<^))))><"):
        print("We have many fish ahoyy!!!")
    elif fishes.count("<^))))><") == (fish * crew).count("<^))))><"):
        print("We have enough fish for everyone.")
    elif (fishes.count("<^))))><") * 2) == (fish * crew).count("<^))))><"):
        print("We can share the fish together Yahoooo!!!")
    else:
        print("No one will eat them  because we cannot be divided the fish.")
main()

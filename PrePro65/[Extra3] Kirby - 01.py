'''Kirby'''

def kenemies(enemies, health, atk, defeat):
    '''enemies'''
    defeated = defeat
    if enemies == "waddle dee":
        ehealth = 2
        ehealth -= atk
        health -= 1
        if health <= 0:
            return defeated, -1, health
        if ehealth <= 0:
            defeated += 1
            return defeated, 1, health
        else:
            return defeated, -2, health
    elif enemies == "waddle doo":
        ehealth = 5
        ehealth -= atk
        health -= 3
        if health <= 0:
            return defeated, -1, health
        if ehealth <= 0:
            defeated += 1
            return defeated, 2, health
        else:
            return defeated, -2, health
    else:
        return dont_fight(enemies, health, atk, defeated)

def dont_fight(enemies, health, atk, defeated):
    '''other'''
    defeat = defeated
    if enemies == "heal":
        health += 2
        return defeat, -2, health
    elif enemies == "none":
        return defeat, -3, health
    elif enemies == "laser ball":
        ehealth = 3
        ehealth -= atk
        health -= 2
        if health <= 0:
            return defeated, -1, health
        if ehealth <= 0:
            defeated += 1
            return defeated, 3, health
        else:
            return defeated, -2, health
    else:
        return defeat, -2, health

def kirby():
    '''lol'''
    health = int(input())
    defeat = 0
    while True:
        role = input()
        if role == "sword":
            atk = 4
        elif role == "magic":
            atk = 2
        elif role == "master":
            atk = 9
        elif role == "sleep":
            atk = 0
        enemies = input()
        defeat, monster, health = kenemies(enemies, health, atk, defeat)
        print("------------")
        if monster == -1:
            print("%d HP left\nGameOver!\nYou had defeated %d enemies" %(health, defeat))
            break
        elif monster == -2:
            print("%d HP left" %health)
            print("------------")
        elif monster == -3:
            print("%d HP left\nKirby won!\nYou had defeated %d enemies" %(health, defeat))
            break
        if monster == 1:
            print("- waddle dee had defeated -\n%d HP left" %health)
            print("------------")
        elif monster == 2:
            print("- waddle doo had defeated -\n%d HP left" %health)
            print("------------")
        elif monster == 3:
            print("- laser ball had defeated -\n%d HP left" %health)
            print("------------")
    print("------------")
kirby()

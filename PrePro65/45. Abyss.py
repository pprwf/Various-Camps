'''Made in Abyss'''

def deep(level):
    '''บอกระดับชั้น'''
    if level >= 0 and level <= 1350:
        print("1st Layer : Edge of the Abyss")
    elif level > 1350 and level <= 2600:
        print("2nd Layer : Forest of Temptation")
    elif level > 2600 and level <= 7000:
        print("3rd Layer : Great Fault")
    elif level > 7000 and level <= 12000:
        print("4th Layer : The Goblets of Giants")
    elif level > 12000 and level <= 13000:
        print("5th Layer : Sea of Corpses")
    elif level > 13000 and level <= 15500:
        print("6th Layer : The Capital of the Unreturned")
    else:
        print("7th Layer : The Final Maelstrom")

def curse(level, decision):
    '''บอกคำสาปที่ได้รับ'''
    if decision == "down":
        print("Curse : -")
    elif level >= 0 and level <= 1350:
        print("Curse : Light dizziness and nausea.")
    elif level > 1350 and level <= 2600:
        print("Curse : Intense nausea, headaches, and numbness of limbs.")
    elif level > 2600 and level <= 7000:
        print("Curse : Vertigo combined with visual and auditory hallucinations.")
    elif level > 7000 and level <= 12000:
        print("Curse : Intense pain throughout the body and bleeding from every orifice.")
    elif level > 12000 and level <= 13000:
        print("Curse : Complete sensory deprivation, confusion and self-harming behavior.")
    elif level > 13000 and level <= 15500:
        print("Curse : Loss of humanity or death, or under specific conditions, the Blessing.")
    else:
        print("Curse : Certain death.")

def abyss():
    '''เกมมันจะออกอะพี่ ซื้อมาเล่นกะผมปะ'''
    name1 = input()
    deep1 = int(input())
    decis1 = input().lower()
    name2 = input()
    deep2 = int(input())
    decis2 = input().lower()
    name3 = input()
    deep3 = int(input())
    decis3 = input().lower()
    print("Name :", name1)
    deep(deep1)
    curse(deep1, decis1)
    print("---")
    print("Name :", name2)
    deep(deep2)
    curse(deep2, decis2)
    print("---")
    print("Name :", name3)
    deep(deep3)
    curse(deep3, decis3)
abyss()

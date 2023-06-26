'''Deep In Abyss'''

def layer(depth, decision, order="", name="", curse=""):
    '''check abyss depth'''
    if 0 <= depth <= 1350:
        order, name, curse = "1st", "Edge of the Abyss", "Light dizziness and nausea."
    elif 1351 <= depth <= 2600:
        order, name = "2nd", "Forest of Temptation"
        curse = "Intense nausea, headaches, and numbness of limbs."
    elif 2601 <= depth <= 7000:
        order, name = "3rd", "Great Fault"
        curse = "Vertigo combined with visual and auditory hallucinations."
    elif 7001 <= depth <= 12000:
        order, name = "4th", "The Goblets of Giants"
        curse = "Intense pain throughout the body and bleeding from every orifice."
    elif 12001 <= depth <= 13000:
        order, name = "5th", "Sea of Corpses"
        curse = "Complete sensory deprivation, confusion and self-harming behavior."
    elif 13001 <= depth <= 15500:
        order, name = "6th", "The Capital of the Unreturned"
        curse = "Loss of humanity or death, or under specific conditions, the Blessing."
    elif 15501 <= depth:
        order, name, curse = "7th", "The Final Maelstrom", "Certain death."
    curse = "-" if decision == "DOWN" else curse
    return order, name, curse

def abyss(name):
    '''main function'''
    order, floor, curse = layer(int(input()), input())
    name2 = input()
    order2, floor2, curse2 = layer(int(input()), input())
    name3 = input()
    order3, floor3, curse3 = layer(int(input()), input())
    print("Name : %s\n%s Layer : %s\nCurse : %s\n---" %(name, order, floor, curse))
    print("Name : %s\n%s Layer : %s\nCurse : %s\n---" %(name2, order2, floor2, curse2))
    print("Name : %s\n%s Layer : %s\nCurse : %s" %(name3, order3, floor3, curse3))
abyss(input())

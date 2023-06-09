'''Dormitory'''

def damages_cost(month, dorm_key, room_key, damages, cost=0):
    '''aj dorm'''
    if month < 12:
        cost += 15000
    if dorm_key == "yes":
        cost += 1000
    if room_key == "yes":
        cost += 500
    cost += damages * 300
    if cost == 0:
        print("You got lucky!")
    else:
        print("Your payment is due, %d Baht" %cost)

damages_cost(int(input()), input().lower(), input().lower(), int(input()))

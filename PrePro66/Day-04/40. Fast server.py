'''Fast server'''

def server(aspeed, atime, bspeed, btime):
    '''Fast server'''
    aspeed *= 0.001 if atime == "Millisecond" else 0.000001 if atime == "Microsecond"\
    else 0.000000001 if atime == "Nanosecond" else 0.000000000001
    bspeed *= 0.001 if btime == "Millisecond" else 0.000001 if btime == "Microsecond"\
    else 0.000000001 if btime == "Nanosecond" else 0.000000000001
    print("Server %s, %.6f second     \nFaster than server %s , %d times" \
        %("B", bspeed, "A", aspeed // bspeed) if aspeed > bspeed else\
        "Server %s, %.6f second     \nFaster than server %s , %d times" \
            %("A", aspeed, "B", bspeed // aspeed) if bspeed > aspeed else "equal")
server(int(input()), input(), int(input()), input())

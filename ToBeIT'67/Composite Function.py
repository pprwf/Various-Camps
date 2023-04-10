def ffx(x):
    return (15 + x - x ** 3) / (x ** 2 / 3 + 11)
def gfx(x):
    return x ** 3 + 4 * x - 1
num = float(input())
func = input().lower()
if func == "gof":
    print("%.2f" %gfx(ffx(num)))
elif func == "fog":
    print("%.2f" %ffx(gfx(num)))

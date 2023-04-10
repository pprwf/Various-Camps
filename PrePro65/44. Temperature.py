'''อุณหภูมิ'''

def celsius(unit, tem):
    '''Nope'''
    if unit.startswith("R"):
        cels = (tem - 491.67) * (5 / 9)
        if unit.endswith("C"):
            print("Celsius = %.2f" %cels)
        elif unit.endswith("K"):
            print("Kelvin = %.2f" %(cels + 273.15))
        elif unit.endswith("F"):
            print("Fahrenheit = %.2f" %(tem - 459.67))
        else:
            print("Rankine = %.2f" %tem)
    else:
        if unit.endswith("F"):
            print("Fahrenheit = %.2f" %(tem * (9 / 5) + 32))
        elif unit.endswith("K"):
            print("Kelvin = %.2f" %(tem + 273.15))
        elif unit.endswith("R"):
            print("Rankine = %.2f" %((tem + 273.15) * (9 / 5)))
        else:
            print("Celsius = %.2f" %tem)

def convert():
    '''แปลงค่า'''
    num = float(input())
    temp = input().upper()
    if temp.startswith("F"):
        cels = (num - 32) * (5 / 9)
        if temp.endswith("C"):
            print("Celsius = %.2f" %cels)
        elif temp.endswith("K"):
            print("Kelvin = %.2f" %(cels + 273.15))
        elif temp.endswith("R"):
            print("Rankine = %.2f" %((cels + 273.15) * (9 / 5)))
        else:
            print("Fahrenheit = %.2f" %num)
    elif temp.startswith("K"):
        cels = num - 273.15
        if temp.endswith("C"):
            print("Celsius = %.2f" %cels)
        elif temp.endswith("F"):
            print("Fahrenheit = %.2f" %(num * (9 / 5) - 459.67))
        elif temp.endswith("R"):
            print("Rankine = %.2f" %((cels + 273.15) * (9 / 5)))
        else:
            print("Kelvin = %.2f" %num)
    else:
        celsius(temp, num)
convert()

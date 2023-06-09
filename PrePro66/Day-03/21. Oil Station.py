'''Oil Station'''

def main(oil, price):
    '''func doc'''
    print("%.2f litre" %oil)
    print("Pay %.2f baht." %(oil * price))
main(float(input()), float(input()))

'''Fibonacci ดูเหมือน Easy'''

def fibo(num):
    '''Fibonacci'''
    return num if num == 0 or num == 1 else fibo(num - 1) + fibo(num - 2)

def main():
    '''mainnacci'''
    print(fibo(int(input())))
main()

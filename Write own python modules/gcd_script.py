def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

if __name__ == "__main__":              #condition is used to to check module is run directly or by import statement
    if gcd(40,12)==4:                   #if it is imported the this code will not execute
        print('Everything is okay')
    else:
        print('GCD is wrong...')

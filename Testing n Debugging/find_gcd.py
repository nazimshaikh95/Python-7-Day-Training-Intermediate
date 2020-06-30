def gcd(a,b):
    ''' find GCD of given two  numbers i.e. a, b
        '''
    if b==0:
        return a
    return gcd(b,a%b)
    

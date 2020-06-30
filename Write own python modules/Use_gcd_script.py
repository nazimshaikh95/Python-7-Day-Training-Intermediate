''' Importing functions from module "gcd_script" '''

from gcd_script import gcd

a = 56
b = 28
res = gcd(a,b)      #use gcd funtion from imported module
#print(res)

# another example

def check_relative_prime(a,b):
    if gcd(a,b)==1:
        print("Yes, %d and %d are relatively prime"%(a,b))
    else:
        print("No, %d and %d are not relatively prime"%(a,b))

check_relative_prime(11,3)

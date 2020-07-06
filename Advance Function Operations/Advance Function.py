
#default arguments
def greetings(greet,name='Nazim'):
    print(greet,name)

#greetings('hello','Abuzar')
#o/p:hello Abuzar

#greetings('Hi')
#o/p:Hi Nazim


###==Key-word Arguments=========================

def marks(first,second,third):
    print("First = %d , Second = %d , Third = %d "%(first,second,third))

#marks(20,15,19)

#marks(first=21,second=22,third=23)

#marks(second=22,third=23,first=21)

#Restict usage of keyword arguments
def marksr(*,first,second,third):
    print("First = %d , Second = %d , Third = %d "%(first,second,third))

#marksr(second=22,first=21,third=23)

#marksr(21,22,23)

###==Arbitrary Arguments========================

def family(*name):              #*same attribute i.e. only name(string)
    print(name)
print("nazim")
print("Nazim","Abuzar")
print("Nazim","Abuzar","Shahin","Gufran","Najma")

##==Arbitrary Number of Keyword Arguments=======

def person(**attributes):       #**number of different attributes(int,str,float,etc.)
    print(attributes)
person(name='Nazim', age=22, height=5.8)    #returns dictionary of attributes
person(weight=49,name='Nazim', age=22, height=5.8)

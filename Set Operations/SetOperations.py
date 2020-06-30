
a = [1,2,4,1,2,7,5,6]
#print(a)

a = set(a)
#print(a)

#create set
b = { 1,2,4,1,5,2 }
#print(b)

#create empty set
c = set()

f = set([1,2,3,5,8])
p = set([2,3,5,7,11,13])
f.add(13)
#print(f)

p.remove(13)
#print(p)

#Union operation
print(f|p)
#or
print(f.union(p))

#Intersection
print(f&p)
print(f.intersection(p))

#Difference
print(f-p)
print(f.difference(p))

#Symmetric difference
print(f ^ p)
print(f.symmetric_difference(p))

a = set([1,2,3,4])
b = set([1,2])
print(b<=a)
print(b.issubset(a))

print(b>=a)
print(b.issuperset(a))

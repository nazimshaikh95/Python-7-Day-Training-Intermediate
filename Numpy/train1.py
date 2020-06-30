file = open('student_record.txt','r')

lst = list()
dic = dict()
for i in file:
    line = i.split(';')
    nm = line[2].split()[0]
    if nm not in dic:
        dic [ nm ] = 1
    else:
        dic [ nm ] = dic[ nm ] + 1
c=0
max_key = None
max_val = None
for i in dic:
    #print(i ,'=', dic[i])
    if max_val is None:
        max_val = dic[i]
        max_key = i
    if dic[i] > max_val:
        max_val = dic[i]
        max_key = i
print('Highly Occured Name:',max_key,' = ', max_val)

for i,j in dic.items():
    s1 = i
    s2 = j
    s = s1,s2
    lst.append(s)

lst1 = list()
for i,j in lst:
    s = j,i
    lst1.append(s)

print('Top 10 Names Occured in File:')
for i in sorted(lst1,reverse = True):
    print(i)
    c = c+1
    if c==10:
        break


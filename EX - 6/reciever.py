f=open("Code.txt","r")
x=f.readline()
print("E Code:",x)
e=open("Original.txt","r")
y=e.readline()
print("O Code:",y)
l=x.strip("[").strip("]").strip(']\n').split(",")
for i in l:
    i.strip(" ")
c=[]
pos=[]
rb=0
for i in range(len(l)):
    if (2**i >= len(l) + i + 1):
        rb = i
        break
for i in range(rb):
    pos.append(2**i)
print("POSITIONS:",pos)
q=[]
for i in l[::-1]:
    if(i==" 1" or i=="1"):
        q.append(1)
    else:
        q.append(0)
for p in pos:
    count = 0
    i = p - 1
    while i < len(l):
        count += q[i:i + p].count(1)
        i += 2 * p
    c.append(0) if count%2==0 else c.append(1)
print("BINARY:",c[::-1])
change = 0
q=q[::-1]
for i in range(len(c[::-1])):
    change+= c[i]*2**i
q[change-1] = 0 if q[change-1] == 1 else 1
print("ERROR:",change)
print("CORRECTED CODE",q)

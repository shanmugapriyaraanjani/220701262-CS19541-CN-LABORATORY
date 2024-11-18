string = input("Enter string:")
s = ''.join(format(ord(i), '08b') for i in string)
rb = 0

for i in range(len(s)):
    if (2**i >= len(s) + i + 1):
        rb = i
        break

m = len(s) + rb
l = []
pos = []
c = 0
s = s[::-1]

for i in range(rb):
    pos.append(2**i)

for i in range(m):
    if (i + 1) in pos:
        l.insert(i, 'p')
    else:
        l.insert(i, int(s[c]))
        c += 1

print("Parity bit positions:", pos)
print("Initial encoded data with 'p' at parity positions:", l)

for p in pos:
    count = 0
    i = p - 1
    while i < m:
        count += l[i:i + p].count(1)
        i += 2 * p
    l[p - 1] = 1 if count % 2 != 0 else 0
print("Final encoded data with parity bits:", l[::-1])
f = open("Code.txt", "w")
f.write(str(l[::-1]))
f.close()
f = open("Original.txt", "w")
f.write(str(l[::-1]))
f.close()

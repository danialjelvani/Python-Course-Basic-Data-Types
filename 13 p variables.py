'''a = input("enter num 1\n")
b = input("enter num 2\n")
# khorujie balayia stringe
c = a + b
d = int(a) + int(b)
print(c, d, sep='\n')'''


import sys
e = 1
f = 2
print('e=', e, 'f=', f)

g = e
e = f
f = g
del g
print('e=', e, 'f=', f)

e, f = f, e
print('e=', e, 'f=', f)

# ba negah dashtn alt va click mishe
# multiple cursor dasht

# ba negah dashtn ctrl + D ham kalameha similar ro select mikone

# peida krdn index ye value tu list

list1 = [20, 19, 18, 19.5, 19.75, 20, 18]
print(list1.index(19.75))
list1[4] = 20
print(list1)


# peida krdn index agar chnta value moshabeh dashtim:
# rahe khodm:
l = [1, 3, 2, 2, 3, 3, 8]

i = 0
l3 = []
for x in l:
    l2 = {x: i}
    i += 1
    print(l2)
    if x == 3:
        l3.append(i-1)
print(l3)

# rahe ali:

q = [1, 3, 2, 2, 3, 3, 8]

for z, y in enumerate(q):
    if y == 3:
        print(z)

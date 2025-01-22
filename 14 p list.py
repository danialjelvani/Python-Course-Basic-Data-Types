# estekhraje second largest number:

a = [1, 45, 265, 25, 358, 45, 12, 31]
print(sorted(a)[-2])


# rahe dovom:
max1 = a[1]
max2 = a[0]

for x in a[2:]:
    if x >= max1:
        max2 = max1
        max1 = x
print(max1, max2)
a.sort()
print(a)

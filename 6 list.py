a = [1, 2, 3, 'danial']
b = [1, 2, [5, 6, 7]]
print([1, 2, 3] == [2, 1, 3], '\n',
      a[3], '\n',
      a[2:], '\n',
      a[::-1], '\n',
      2 in a, '\n',
      a+a, '\n',
      a+[6, 8], '\n',
      a*2, '\n',
      b[2], '\n',
      b[2][1:],
      )
a[0] = 3
print(a)
del a[0]
print(a)
a[1:] = [4, 4, 4]
print(a)
a.append([3])
a.append(3)
print(a)

# vase copy inkaro mikonim [:] chon list taghir mikone:
list1 = [1, 2]
list2 = list1
list2[0] = 90
print(list2, list1)

# b hamin khater copysh mikonim k list1 taghir nkne
list3 = [1, 2]
list4 = list3[:]
list4[0] = 90
print(list4, list3)

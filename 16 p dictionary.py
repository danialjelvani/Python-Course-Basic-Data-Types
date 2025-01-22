# merge dictionaries:

d1 = {'name': 'danial', 'age': 30}
d2 = {'nationality': 'iranian'}
d4 = {'age': 31}
d3 = {**d1, **d2}
print(d3)
d1.update(d4)
print(d1)


list1 = [2, 1, 3, 5, 3, 2]

setlist1 = set(list1)
print(setlist1)
for x in list1:
    if x in setlist1:
        print(x)
        break
    else:
        print('no duplicates in list')

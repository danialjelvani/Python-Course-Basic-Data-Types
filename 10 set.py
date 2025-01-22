# set mese dic ba {} e vali tekrari nadare
# set key o value nadare
set1 = {1, 1, 1, 2, 2, 3}
print(set1, type(set1))

# bejaye append add dare
set1.add(4)
print(set1)

# bejaye extend update dare
set1.update([7, 8, 9])
print(set1)

# mishe tekrariaro hazf krd
list = [2, 3, 3, 3]
print(set(list))

# set ha baham jam nmishn union midim
set2 = set1.union({0, 1, 2, 3, 5})
print(set2)

# eshterak ba intersection
set3 = set2.intersection({7, 8, 9})
print(set3)

# difference baese hazf mishe
print(set3.difference({9}))

print(set('danial'))

set1.remove(2)
print(set1)

# set baraye search date behtarine
# set o dic hashable an yani tabdil b binary mikoneo lookup mikone tu ram
# frozenset  dg taghir nmikone mese tuple


fset = frozenset({6, 3, 1})
fset2 = fset.union({5, 9})
print(fset, fset2)

# chon frozensettaghir nmikone mitune pas key tu dic bashe
dic1 = {
    frozenset({1, 2, 3}): 4,
    frozenset({2, 9}): 5
}
print(dic1[frozenset({2, 9})])

print(hash('danial'))

# raveshe 1:

s = {
    'ali': 17,
    'danial': 19.75,
    'mahsa': 20,
}

# raveshe 2:

s1 = dict(
    ali=17,
    danial=19.75,
    mahsa=20,
)
print(s1['danial'])

# injuri index mikonim ba key

s1['danial'] = 20
print(s1)

# dg append nadareo mese payin add mikonim

s1['amir'] = 18
print(s1)

for x in s1:
    print(x)

print('\n', s1.keys())
print('\n', s1.values())

s1['5'] = [145, 'a']
print(s1)

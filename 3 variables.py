a = 100
b = 100
print(id(a,), id(b))
print(a is b)
print(a == b)

a = 300000009999999999
b = 300000009999999999
print(id(a), id(b))
print(hex(id(a)) == hex(id(b)))
print(a is b)
print(a == b)

# (==) faghat barabarie meghdar vasash moheme vali (is) gheiraz meghdar id ro ham check mikoneh

help("keywords")

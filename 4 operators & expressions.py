print(5 % 2, 5//2, 5/2, 3**3)

print(3 == 4, 3 != 4)

a = 1.1 + 2.2
c = 3.3
print(a == c)

# ye tolerance bayad taeen knim chon python 1.1 o 2.2 o 3.3 ro
# binary mikone va yeki nmishn  masalan inja 0.00001 ro tolerance grftm

print(abs(a-c) < 0.00001)

print(not (3 == 4))


name = input()
if not name:
    print('name is required')
else:
    print(name, 'is ur name')

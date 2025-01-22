import sys
print(sys.getsizeof(1))
a = "ali"
print(sys.getsizeof(a))
print(sys.getsizeof("a"))

# 0x = hexadecimal
print(0x12)

print(type(1.3))

print(4e3)
print(0.1 + 0.2 == 0.3)
print(abs(-4.5))
print('ali'*2)
print('''bashe pas
berim
khate bad''')
# age nakhaim escape seq. ro emal kone ghable string r mizarim
print(r'da\nial')
print(bool([]))
print(bool(0))
print(bool({}))
print(bool(''))
print(bool(None))
print(bool([5, 3]))
print(divmod(7, 3))
print(pow(2, 3))
print(round(4.5))
a = []
for x in range(11):
    a.append(x)
print(a)

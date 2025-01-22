
import time
a = (1, 2, 3, 4)
# tuple does no support del modify append ...
print(type((1)), '\n',
      type((1,)))
b = list('ali')
c = list((1, 2, 3))
d = tuple[1, 2, 3]
print(b, c, d)

t = (5, 6, 7, 8)
n1, n2, n3, n4 = t
print(n2)

# dar asl in zir inaro tuple mikone pishe khodesho
# badesh unpack mikoneh
x, y, z = 11, 12, 13
print(y)

z = (4, 5, 6, 7, 8, 9, 10, 11, 12)
m1, m2, *h = z
print(m1, '\n',
      m2, '\n',
      h)
o = [1, 1, 1]
o.append(2)
print(o)
o.append([3, 4, 5])
print(o)
o.extend([3, 3, 6])
print(o)

print(int(float(19.75)))
print(round(19.75))

start_time = time.time()
w = 3**455444
print(round(time.time()-start_time, 10))

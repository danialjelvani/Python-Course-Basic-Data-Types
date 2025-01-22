from array import array
n = 10
for i in range(n):
    for j in range(n):
        print(f'{i*j:3}', end=' ')

# big-O complexity chart
# O(2^n), O(n^2), O(nlog n), O(n), O(log n), O(1)(havapeima)


a = array('i', [1, 2, 3, 5, 9])
# array hajme sabete kamtar az list migire
# faghat bayad hamgen bashe array

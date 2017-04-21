print(' '.join([str(i) for i in range(1, 101)]))
k = []
for i in range(1, 101):
    if i % 15 == 0:
        k.append('BazQux')
    elif i % 3 == 0:
        k.append('Baz')
    elif i % 5 == 0:
        k.append('Qux')
    else:
        k.append(i)
print(' '.join([str(i) for i in k]))

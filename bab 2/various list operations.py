L1 = [2,1,3]
L2 = [4,5,6]
L3 = L1 + L2
L1.extend([0,6])

L = [2,1,3,6,3,7,0]
L.remove(2)
L.remove(3)
del(L[1])
print(L.pop())

s = "I<3 cs"
print(list(s))
print(s.split('<'))
L = ['a', 'b', 'c']
print(''.join(L))
print('_'.join(L))

L=[9,6,0,3]
print(sorted(L))
L.sort()
L.reverse()

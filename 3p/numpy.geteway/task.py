import numpy as np

a = np.array(
    [[1],[1],[1],[1],[1]]
    ,dtype =float)

a[2] = 3.14
b = a.copy()
b = b.T
c = np.dot(a ,b)
d = np.random.rand(10,1)
e = np.random.normal(10,2,size = (2,5))
f = e[:,1]
g = e[:,2:4]
h = np.random.rand(5,2)
i = np.dot(e,h)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
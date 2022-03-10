import os

path = 'C:\\Users\\Timo\\Desktop\\错题\\图推'

f = os.listdir(path)
n = 0

for i in f:
    old = path + '\\' + f[n]
    new = path + '\\' + '图推' + str(n) + '.jpg'
    os.rename(old,new)
    n+=1


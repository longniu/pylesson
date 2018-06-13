# sorf function
''''
def size(item):
    sizelist = ['L','M','S','XS']
    pos = sizelist.index(item)
    return pos

data = ['S','M','XS','L','M','M','XS','S','M','L','M']
data.sort(key = size)
print(data)

'''

sizelist = ['L','M','S','XS']
data = ['S','M','XS','L','M','M','XS','S','M','L','M']
data.sort(key = lambda item : sizelist.index(item))
print(data)

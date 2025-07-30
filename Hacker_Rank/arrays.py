import numpy


def arrays(arr):
    myarr = numpy.array(arr, dtype='f')
    return myarr[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

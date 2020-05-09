import numpy

def arrays(arr):
    ar = numpy.array(arr, float)
    return  ar[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
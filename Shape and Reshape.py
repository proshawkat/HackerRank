import numpy

inp = list(map(int, input().split()))
arr = numpy.array(inp)
newarr = arr.reshape(3, 3)
print(newarr)
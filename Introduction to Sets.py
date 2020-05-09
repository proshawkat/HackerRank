def average(array):
    x = set(array)
    s = sum(x)
    l = len(x)
    result = s/l
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


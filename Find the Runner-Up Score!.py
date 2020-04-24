if __name__ == '__main__':
    n = int(input())
    l = list()
    arr = map(int, input().split())
    for i in arr:
        l.append(i)
    x = sorted(set(l))[-2]
    print(x)
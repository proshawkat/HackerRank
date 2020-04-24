if __name__ == '__main__':
    n = int(input())
    l = list()
    integer_list = map(int, input().split())
    for x in integer_list:
        l.append(int(x))
    t = tuple(l)
    print(hash(t))

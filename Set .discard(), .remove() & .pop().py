n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    x = input().split()
    if x[0] == 'pop':
        s.pop()
    elif x[0] == 'remove':
        s.remove(int(x[1]))
    elif x[0] == 'discard':
        s.discard(int(x[1]))

print(sum(list(s)))
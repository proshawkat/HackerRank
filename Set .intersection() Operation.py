r1 = int(input())
int1 = input().split()
set1 = set(map(int, int1))

r2 = int(input())
int2 = input().split()
set2 = set(map(int, int2))

z = set1.intersection(set2)
print(len(z))
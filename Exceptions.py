N = int(input())
for i in range(N):
    a, b = input().split()

    try:
        x = int(a) // int(b)
        print(x)
    except ValueError as err:
        print("Error Code:", err)
    except ZeroDivisionError:
        print('Error Code: integer division or modulo by zero')
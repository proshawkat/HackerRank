def print_formatted(number):
    for i in range(number):
        i += 1
        d = i
        o = oct(i)[2:]
        h = hex(i).upper()[2:]
        b = bin(i)[2:]
        width = len(bin(number)[2:])
        print(str(d).rjust(width), str(o).rjust(width),  str(h).rjust(width), str(b).rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
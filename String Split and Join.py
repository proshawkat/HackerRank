def split_and_join(line):
    str = line.split(" ")
    str = ("-").join(str)
    return str

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
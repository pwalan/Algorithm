import sys

if __name__ == "__main__":
    for line in sys.stdin:
        a = line.split()
        x, y = int(a[0]), int(a[1])
        while x != y:
            if x < y:
                y = y >> 1
            else:
                x = x >> 1
        print(x)

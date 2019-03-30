from sys import stdin, stdout

def main():
    sum = 0

    for num in stdin:
        sum += int(num)

    print(sum)


if __name__ == "__main__":
    main()

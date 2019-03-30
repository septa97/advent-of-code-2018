from sys import stdin, stdout

def main():
    twos = 0
    threes = 0

    for s in stdin:
        count_map = {}

        for c in s:
            if c in count_map:
                count_map[c] += 1
            else:
                count_map[c] = 1

        two = False
        three = False
        for k, v in count_map.items():
            if v == 2:
                two = True
            elif v == 3:
                three = True

        if two:
            twos += 1

        if three:
            threes += 1

    print(twos * threes)


if __name__ == "__main__":
    main()

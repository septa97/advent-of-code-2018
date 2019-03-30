from sys import stdin

def main():
    ids = []

    for s in stdin:
        ids.append(s)

    for i in range(len(ids)):
        for j in range(i+1, len(ids)):
            a = ids[i]
            b = ids[j]
            diff = 0
            last_diff = -1

            for c in range(len(a)):
                if ord(a[c]) - ord(b[c]) != 0:
                    diff += 1
                    last_diff = c

                if diff > 1:
                    break

            if diff == 1:
                print(a[:last_diff] + a[last_diff+1:])
                return

if __name__ == "__main__":
    main()

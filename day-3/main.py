from sys import stdin

def main():
    MAX_WIDTH = -1
    MAX_HEIGHT = -1
    left_diff = []
    top_diff = []
    width = []
    height = []

    for line in stdin:
        [_, _, lt, wh] = line.split()

        lt = lt[:-1]
        lt_split = lt.split(',')
        wh_split = wh.split('x')

        a = int(lt_split[0])
        b = int(lt_split[1])
        c = int(wh_split[0])
        d = int(wh_split[1])
        left_diff.append(a)
        top_diff.append(b)

        width.append(c)
        height.append(d)

        MAX_WIDTH = max(a+c, MAX_WIDTH)
        MAX_HEIGHT = max(b+d, MAX_HEIGHT)

    arr = [[0 for j in range(MAX_WIDTH)] for i in range(MAX_HEIGHT)]
    marker = [[False for j in range(MAX_WIDTH)] for i in range(MAX_HEIGHT)]
    ans = 0

    for c in range(len(left_diff)):
        for i in range(top_diff[c], top_diff[c]+height[c]):
            for j in range(left_diff[c], left_diff[c]+width[c]):
                arr[i][j] += 1

                if arr[i][j] >= 2:
                    if not marker[i][j]:
                        ans += 1

                    marker[i][j] = True

    print(ans)

if __name__ == "__main__":
    main()

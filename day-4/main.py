from sys import stdin

def main():
    details = []

    for line in stdin:
        [time, detail] = line.split(']')

        time = time[1:]
        detail = detail.strip()

        details.append((time, detail))

    details = sorted(details, key=lambda detail: detail[0])

    guard_time = {}
    i = 0

    while i < len(details):
        curr = details[i]

        if curr[1].startswith("Guard #"):
            guard_id = curr[1].split()[1][1:]

            if guard_id not in guard_time:
                guard_time[guard_id] = [0 for c in range(60)]

            i += 1

            while i < len(details) and not details[i][1].startswith("Guard #"):
                action = details[i][1]

                start = int(details[i-1][0][-2:])
                end = int(details[i][0][-2:])

                if action == "wakes up":
                    sleep_time = guard_time[guard_id]

                    for j in range(start, end):
                        sleep_time[j] += 1

                i += 1

    # computation for part 1
    max_sleep = -1
    guard_id_max = "-1"

    for k, v in guard_time.items():
        curr_sum = sum(v)
        if curr_sum > max_sleep:
            max_sleep = curr_sum
            guard_id_max = k

    max_index = -1
    max_guard_sleep = -1

    for i in range(60):
        if guard_time[guard_id_max][i] > max_guard_sleep:
            max_guard_sleep = guard_time[guard_id_max][i]
            max_index = i

    # part 1 answer
    print(int(guard_id_max) * max_index)

    # computation for part 2
    max_per_minute = []

    for i in range(60):
        minute_max = -1
        guard_max = "-1"

        for k in guard_time.keys():
            if guard_time[k][i] > minute_max:
                minute_max = guard_time[k][i]
                guard_max = k

        max_per_minute.append((guard_max, minute_max))

    overall_minute_max = -1
    index_max = -1

    for i in range(60):
        if max_per_minute[i][1] > overall_minute_max:
            overall_minute_max = max_per_minute[i][1]
            index_max = i

    # part 2 answer
    print(int(max_per_minute[index_max][0]) * index_max)

if __name__ == "__main__":
    main()

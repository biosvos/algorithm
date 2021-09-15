def solution(clothes):
    d = {}
    for cloth in clothes:
        n = d.get(cloth[1], 0)
        d[cloth[1]] = n + 1
    values = list(d.values())

    # print(f"values: {values}")

    prev = [1]

    for i in range(len(values)):
        cur = []
        for j in range(2 ** (i + 1)):
            if j % 2 == 0:  # left
                cur.append(prev[j // 2])
            else:  # right
                cur.append(prev[j // 2] * values[i])

        # print(cur)
        prev = cur
    return sum(prev) - 1


def main2():
    arr = [0, 1, 2, 3, 4, 5]

    for i in range(2 ** len(arr)):
        t = []
        for j in range(len(arr)):
            if i & 2 ** j:
                t.append(arr[j])
        print(t)


def main():
    assert solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]) == 5
    assert solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]) == 3


if __name__ == '__main__':
    main()

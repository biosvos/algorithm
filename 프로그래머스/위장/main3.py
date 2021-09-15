def solution(clothes):
    d = {}
    for cloth in clothes:
        n = d.get(cloth[1], 0)
        d[cloth[1]] = n + 1
    values = list(d.values())
    # values = [1, 2, 3, 4, 5]

    # print(f"values: {values}")

    arr = [0] * (2 ** (len(values) + 1))
    # print(arr)

    # print("start idx")
    start_idx = [2 ** idx for idx in range(2, len(values) + 2)]
    # print(start_idx)

    # arr[1] = 1
    # print(arr)
    level = 0
    for idx in range(2, 2 ** (len(values) + 1)):
        if idx >= start_idx[0]:
            start_idx.pop(0)
            level += 1

        # print(f"{idx}: level {level}")
        if idx % 2 == 0:  # left
            arr[idx] = arr[idx // 2]
        else:  # right
            if arr[idx // 2] == 0:
                arr[idx] = values[level]
            else:
                arr[idx] = arr[idx // 2] * values[level]

    return sum(arr[2 ** len(values):])


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

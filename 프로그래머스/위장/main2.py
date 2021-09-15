def multi(nums: list):
    ret = 1
    for n in nums:
        ret *= n

    return ret


def solution(clothes):
    d = {}
    for cloth in clothes:
        n = d.get(cloth[1], 0)
        d[cloth[1]] = n + 1
    values = list(d.values())

    return sum([multi([values[j] for j in range(len(values)) if i & 2 ** j]) for i in range(1, 2 ** len(values))])


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

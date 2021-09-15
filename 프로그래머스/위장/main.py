import itertools


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
    values = d.values()

    ret = 0
    for idx in range(1, len(values) + 1):
        for item in itertools.combinations(values, idx):
            ret += multi(item)
    return ret


def main():
    assert solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]) == 5
    assert solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]) == 3


if __name__ == '__main__':
    main()

def multi(nums):
    ret = 1
    for n in nums:
        ret *= n

    return ret


def solution(clothes):
    d = {}
    for cloth in clothes:
        n = d.get(cloth[1], 1)
        d[cloth[1]] = n + 1

    return multi(d.values()) - 1


def main():
    assert solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]) == 5
    assert solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]) == 3


if __name__ == '__main__':
    main()

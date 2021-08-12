import collections
import itertools


def solution(orders, course):
    orders = [set(order) for order in orders]
    orders.sort(key=lambda x: len(x))
    answer = []

    for c in course:
        drop_while(lambda x: len(x) < c, orders)
        if not orders:
            break

        ret = combination(c, orders)
        if not ret:
            break

        answer.extend(most_count(ret))

    answer.sort()
    return answer


def most_count(arr):
    ret = []
    counters = collections.Counter(arr)
    items = iter(counters.most_common())
    most_item = next(items)

    ret.append(most_item[0])
    for item in items:
        if most_item[1] == item[1]:
            ret.append(item[0])
        else:
            break

    return ret


def combination(window_size, orders) -> list:
    n = len(orders)
    ret = []
    for i in range(n - 1):
        for window in itertools.combinations(orders[i], window_size):
            com = set(window)
            for j in range(i + 1, n):
                if len(com - orders[j]) == 0:
                    ret.append(''.join(sorted(com)))
    return ret


def drop_while(fn, arr: list):
    while arr:
        if not fn(arr[0]):
            return

        del arr[0]


def main():
    assert solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]) == ["AC", "ACDE", "BCFG", "CDE"]
    assert solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]) == ["ACD", "AD", "ADE", "CD", "XYZ"]
    assert solution(["XYZ", "XWY", "WXA"], [2, 3, 4]) == ["WX", "XY"]


if __name__ == '__main__':
    main()

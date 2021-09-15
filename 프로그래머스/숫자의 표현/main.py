import math


def continuous_sum(start, end):
    return (start + end) * (end - start + 1) // 2


def solution(n):
    ret = 1  # 자기 자신
    end = math.ceil(n / 2)
    start = end - 1
    print(end)

    while start >= 0:
        r = continuous_sum(start, end)
        if r > n:
            end -= 1
            # if start >= end:
            #     start -= 1
        elif r == n:
            end -= 1
            ret += 1
        else:
            start -= 1
        # print(start, end)

    return ret
    # print(ret)


def main():
    assert solution(15) == 4
    assert solution(19) == 4


if __name__ == '__main__':
    main()

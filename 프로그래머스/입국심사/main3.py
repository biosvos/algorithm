def solution(n, times):
    times.sort()
    up = times[0] * n

    print(up)


def main():
    assert solution(6, [7, 10]) == 28
    assert solution(6, [1, 9]) == 6
    assert solution(10, [1, 10]) == 10
    assert solution(11, [1, 10]) == 10


if __name__ == '__main__':
    main()

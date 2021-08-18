def solution(left, right):
    return sum(n if number_of_divisor(n) % 2 == 0 else -n for n in range(left, right + 1))


def number_of_divisor(n):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
    return cnt


def main():
    assert solution(13, 17) == 43
    assert solution(24, 27) == 52


if __name__ == '__main__':
    main()

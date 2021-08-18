def gcd(a: int, b: int) -> int:
    if b > a:
        a, b = b, a

    while b != 0:
        b, a = a % b, b

    return a


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def solution(n, m):
    return [gcd(n, m), lcm(n, m)]


def main():
    assert solution(3, 12) == [3, 12]
    assert solution(2, 5) == [1, 10]


if __name__ == '__main__':
    main()

def is_prime(n):
    if n < 2:
        return False

    sq = int(n ** 0.5)
    for i in range(2, sq + 1):
        if n % i == 0:
            return False

    return True


def solution(n):
    answer = 0
    for i in range(2, n + 1):
        if is_prime(i):
            answer += 1
    return answer


def main():
    assert solution(10) == 4
    assert solution(5) == 3


if __name__ == '__main__':
    main()

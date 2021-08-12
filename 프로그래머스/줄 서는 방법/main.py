import math


def solution(n, k):
    answer = []
    inp = list(range(1, n + 1))
    k -= 1
    fact = math.factorial(n)

    while len(inp) > 0:
        fact //= n
        n -= 1
        choice, k = divmod(k, fact)
        answer.append(inp.pop(choice))

    return answer


def main():
    assert solution(3, 1) == [1, 2, 3]
    assert solution(3, 2) == [1, 3, 2]
    assert solution(3, 3) == [2, 1, 3]
    assert solution(3, 4) == [2, 3, 1]
    assert solution(3, 5) == [3, 1, 2]
    assert solution(3, 6) == [3, 2, 1]


if __name__ == '__main__':
    main()

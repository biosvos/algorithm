def permute(numbers, left, right):
    if left == right:
        for i in range(len(numbers)):
            yield int(''.join(numbers[:i + 1]))
        return

    for i in range(left, right + 1):
        numbers[i], numbers[left] = numbers[left], numbers[i]
        if numbers[0] != '0':
            yield from permute(numbers, left + 1, right)
        numbers[i], numbers[left] = numbers[left], numbers[i]


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def solution(numbers):
    lst = list(numbers)
    cache = set()
    ret = 0
    for item in permute(lst, 0, len(lst) - 1):
        if item not in cache:
            cache.add(item)
            if is_prime(item):
                ret += 1

    return ret


def main():
    assert solution("011") == 2
    assert solution("17") == 3


if __name__ == '__main__':
    main()

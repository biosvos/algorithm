import itertools


def solution(numbers):
    numbers = [str(n) for n in numbers]
    return max(''.join(item) for item in itertools.permutations(numbers))


def main():
    assert solution([6, 10, 2]) == "6210"
    assert solution([3, 30, 34, 5, 9]) == "9534330"
    assert solution([100, 10]) == "10100"
    assert solution([24, 244]) == "24424"


if __name__ == '__main__':
    main()

def solution(numbers):
    return sum(set(range(1, 10)) - set(numbers))


def main():
    assert solution([1, 2, 3, 4, 6, 7, 8, 0]) == 14
    assert solution([5, 8, 4, 0, 6, 7, 9]) == 6


if __name__ == '__main__':
    main()

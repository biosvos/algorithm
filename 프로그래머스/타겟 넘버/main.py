def sol(arr, target, total):
    arr = list(arr)
    if not arr:
        if total == target:
            return 1
        return 0

    item = arr.pop()
    return sol(arr, target, total + item) + sol(arr, target, total - item)


def solution(numbers, target):
    return sol(numbers, target, 0)


def main():
    assert solution([1, 1, 1, 1, 1], 3) == 5


if __name__ == '__main__':
    main()

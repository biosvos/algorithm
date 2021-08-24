def solution(nums):
    return min(len(nums) // 2, len(set(nums)))


def main():
    assert solution([3, 1, 2, 3]) == 2
    assert solution([3, 3, 3, 2, 2, 4]) == 3
    assert solution([3, 3, 3, 2, 2, 2]) == 2


if __name__ == '__main__':
    main()

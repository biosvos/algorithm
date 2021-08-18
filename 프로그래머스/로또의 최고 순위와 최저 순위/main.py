def solution(lotto_nums, win_nums):
    lotto_set = set(lotto_nums) - {0}
    win_set = set(win_nums)
    correct = len(lotto_set & win_set)
    unknown = 6 - len(lotto_set)
    return [min(7 - correct - unknown, 6), min(7 - correct, 6)]


def main():
    assert solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]) == [3, 5]
    assert solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]) == [1, 6]
    assert solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]) == [1, 1]


if __name__ == '__main__':
    main()

def rec(triangle: list, i, j, acc):
    if len(triangle) == i:
        return acc

    return max(rec(triangle, i + 1, j, acc + triangle[i][j]), rec(triangle, i + 1, j + 1, acc + triangle[i][j]))


def solution(triangle):
    return rec(triangle, 0, 0, 0)


def main():
    assert solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]) == 30


if __name__ == '__main__':
    main()

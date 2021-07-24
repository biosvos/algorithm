def solution(arr):
    if len(arr) < 2:
        return [-1]

    min_idx = 0
    min_x = arr[0]
    for i, x in enumerate(arr):
        if min_x > x:
            min_x = x
            min_idx = i

    del arr[min_idx]
    return arr


def main():
    assert solution([4, 3, 2, 1]) == [4, 3, 2]
    assert solution([10]) == [-1]


if __name__ == '__main__':
    main()

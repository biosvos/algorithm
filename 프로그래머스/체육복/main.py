def solution(n, lost, reverse):
    lost_set = set(lost)
    reverse_set = set(reverse)
    inter = lost_set & reverse_set
    lost_set = lost_set - inter
    reverse_set = reverse_set - inter
    for r in reverse_set:
        if r - 1 in lost_set:
            lost_set.remove(r - 1)
        elif r + 1 in lost_set:
            lost_set.remove(r + 1)

    return n - len(lost_set)


def main():
    assert solution(5, [2, 4], [1, 3, 5]) == 5
    assert solution(5, [1, 3, 5], [2, 4]) == 4
    assert solution(5, [1, 3, 5], [2]) == 3
    assert solution(5, [2, 4], [3]) == 4
    assert solution(3, [3], [1]) == 2


if __name__ == '__main__':
    main()

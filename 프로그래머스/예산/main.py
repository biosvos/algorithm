def solution(d, budget):
    d = sorted(d)
    n = 0
    for x in d:
        budget -= x
        if budget < 0:
            break

        n += 1

    return n


def main():
    assert solution([1, 3, 2, 5, 4], 9) == 3
    assert solution([2, 2, 3, 3], 10) == 4


if __name__ == '__main__':
    main()

def solution(land):
    while len(land) > 1:
        item = land.pop()
        item_idx = sorted([(item, idx) for idx, item in enumerate(item)], reverse=True, key=lambda x: x[0])
        first = item_idx[0]
        second = item_idx[1]
        for i in range(len(land[-1])):
            if i != first[1]:
                land[-1][i] += first[0]
            else:
                land[-1][i] += second[0]

    return max(land[0])


def main():
    assert solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]) == 16


if __name__ == '__main__':
    main()

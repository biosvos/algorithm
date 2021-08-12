def solution(priorities, location):
    q = list(enumerate(priorities))
    cnt = 0
    while item := q.pop(0):
        if not q:
            cnt += 1
            return cnt

        max_priority = max(q, key=lambda x: x[1])
        if item[1] < max_priority[1]:
            q.append(item)
        else:
            cnt += 1
            if item[0] == location:
                return cnt


def main():
    assert solution([2], 0) == 1
    assert solution([2, 1, 3, 2], 2) == 1
    assert solution([1, 1, 9, 1, 1, 1], 0) == 5


if __name__ == '__main__':
    main()

def solution(x, n):
    answer = []
    acc = 0
    for _ in range(n):
        acc += x
        answer.append(acc)
    return answer


def main():
    assert solution(2, 5) == [2, 4, 6, 8, 10]


if __name__ == '__main__':
    main()

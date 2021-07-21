def solution(arr):
    answer = []
    if len(arr) == 0:
        return answer

    prev_n = arr[0]
    for n in arr:
        if prev_n != n:
            answer.append(prev_n)
            prev_n = n

    answer.append(prev_n)

    return answer


def main():
    print(solution([1, 1, 3, 3, 0, 1, 1]))
    print(solution([4, 4, 4, 3, 3]))


if __name__ == '__main__':
    main()

def solution(arr, divisor):
    answer = [x for x in arr if x % divisor == 0]
    if len(answer) == 0:
        return [-1]
    answer.sort()
    return answer


def main():
    assert solution([5, 9, 7, 10], 5) == [5, 10]


if __name__ == '__main__':
    main()

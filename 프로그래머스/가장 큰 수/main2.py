import itertools


def solution(numbers):
    numbers = sorted([str(n) for n in numbers], reverse=True)
    arr = [list() for _ in range(10)]
    for n in numbers:
        idx = int(n[0])
        arr[idx].append(n)

    answer = ''
    for item in reversed(arr):
        answer += max(''.join(tp) for tp in itertools.permutations(item))

    return answer
    # print(numbers)
    # return max(''.join(item) for item in itertools.permutations(numbers))


def main():
    assert solution([3, 30, 34, 5, 9]) == "9534330"
    assert solution([6, 10, 2]) == "6210"
    assert solution([100, 10]) == "10100"
    assert solution([24, 244]) == "24424"


if __name__ == '__main__':
    main()

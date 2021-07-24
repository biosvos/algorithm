def solution(array, commands):
    answer = []
    for x, y, z in commands:
        a = array[x-1:y]
        a.sort()
        answer.append(a[z-1])
    return answer


def main():
    assert solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]) == [5, 6, 3]


if __name__ == '__main__':
    main()

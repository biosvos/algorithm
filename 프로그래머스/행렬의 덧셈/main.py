def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        sub = []
        for j in range(len(arr1[i])):
            sub.append(arr1[i][j] + arr2[i][j])
        answer.append(sub)
    return answer


def main():
    assert solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]) == [[4, 6], [7, 9]]
    assert solution([[1], [2]], [[3], [4]]) == [[4], [6]]


if __name__ == '__main__':
    main()

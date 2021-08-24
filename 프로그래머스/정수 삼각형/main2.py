def solution(triangle):
    while len(triangle) > 1:
        bottom = triangle.pop()
        for i in range(len(bottom)-1):
            m = max(bottom[i:i+2])
            triangle[-1][i] += m

    return triangle[0][0]


def main():
    assert solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]) == 30


if __name__ == '__main__':
    main()

import math


def solution(progresses, speeds):
    answer = []

    release = 0
    cnt = 0
    for p, s in zip(progresses, speeds):
        r = math.ceil((100 - p) / s)
        if release < r:
            if cnt > 0:
                answer.append(cnt)
            release = r
            cnt = 1
        else:
            cnt += 1

    answer.append(cnt)

    return answer


def main():
    assert solution([93, 30, 55], [1, 30, 5]) == [2, 1]
    assert solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]) == [1, 3, 2]


if __name__ == '__main__':
    main()

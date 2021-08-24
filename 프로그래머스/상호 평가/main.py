grade = ['F', 'F', 'F', 'F', 'F', 'D', 'D', 'C', 'B', 'A', 'A']
#         0    1    2    3    4    5    6    7    8    9    10


def solution(scores):
    answer = ''
    nr_student = len(scores)
    for i in range(nr_student):
        me = scores[i][i]
        up = me
        down = me
        same = 0
        avg = 0.0
        for j in range(nr_student):
            avg += scores[j][i]
            if scores[j][i] == me:
                same += 1
            if scores[j][i] > up:
                up = scores[j][i]
            if scores[j][i] < down:
                down = scores[j][i]

        if same == 1 and (up == me or down == me):
            avg -= me
            avg /= (nr_student - 1)
        else:
            avg /= nr_student
        answer += grade[int(avg // 10)]

    return answer


def main():
    assert solution([[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67], [61, 57, 100, 80, 65],
                     [24, 90, 94, 75, 65]]) == "FBABD"
    assert solution([[50, 90], [50, 87]]) == "DA"
    assert solution([[70, 49, 90], [68, 50, 38], [73, 31, 100]]) == "CFD"


if __name__ == '__main__':
    main()

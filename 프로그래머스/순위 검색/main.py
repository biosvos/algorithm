def match(applicant, query):
    for a, q in zip(applicant[0], query[0]):
        if q == '-':
            continue
        if a != q:
            return False

    return applicant[1] >= query[1]


def solution(info, query):
    # convert
    info = [i.split(" ") for i in info]
    info = [[i[:-1], int(i[-1])] for i in info]  # [[조건...], 점수]
    query = [q.replace("and ", "").split(" ") for q in query]
    query = [[q[:-1], int(q[-1])] for q in query]  # [[조건...], 점수]

    return [len([None for applicant in info if match(applicant, qry)]) for qry in query]


def main():
    assert solution([
        "java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"
    ], [
        "java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
        "- and - and - and - 150"
    ]) == [1, 1, 1, 1, 2, 4]


if __name__ == '__main__':
    main()

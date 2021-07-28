import itertools


def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    scores = []
    for pattern in patterns:
        scores.append(len([1 for a, b in zip(answers, itertools.cycle(pattern)) if a == b]))

    answer = []
    max_score = 0
    for i, score in enumerate(scores, start=1):
        if score > max_score:
            max_score = score
            answer.clear()
            answer.append(i)
        elif score == max_score:
            answer.append(i)

    return answer


def main():
    assert solution([1, 2, 3, 4, 5]) == [1]
    assert solution([1, 3, 2, 4, 2]) == [1, 2, 3]


if __name__ == '__main__':
    main()

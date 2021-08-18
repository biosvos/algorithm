import re


class Score:
    num: int
    upper: int
    option: str

    def __init__(self):
        self.option = ''


def dart_iter(dart_result: str):
    p = re.compile("([0-9]+)([SDT])([*#]?)")
    dart = p.findall(dart_result)
    print(dart)

    for d in dart:
        yield d


def solution(dart_result):
    scores = []
    for rec in dart_iter(dart_result):
        scores.append(rec.num ** rec.upper)
        if rec.option == "#":
            scores[-1] *= -1
        elif rec.option == "*":
            scores[-1] *= 2
            if len(scores) > 1:
                scores[-2] *= 2

    return sum(scores)


def main():
    assert solution("1S2D*3T") == 37
    assert solution("1D2S#10S") == 9
    assert solution("1D2S0T") == 3
    assert solution("1S*2T*3S") == 23
    assert solution("1D#2S*3S") == 5
    assert solution("1T2D3D#") == -4
    assert solution("1D2S3T*") == 59


if __name__ == '__main__':
    main()

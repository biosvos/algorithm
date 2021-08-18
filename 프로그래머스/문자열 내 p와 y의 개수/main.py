def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y')


def main():
    assert solution("pPoooyY")
    assert not solution("Pyy")


if __name__ == '__main__':
    main()

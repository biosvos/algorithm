def up_down(ch: str):
    return 13 - abs(ord(ch) - 78)


def move(conv: list):
    l_zero = 0
    r_zero = 0
    for item in conv:
        if item != 0:
            break
        l_zero += 1
    for item in reversed(conv):
        if item != 0:
            break
        r_zero += 1
    middle = len(conv) - l_zero - r_zero
    if middle == 0:
        return 0

    return min(l_zero + middle, r_zero + middle, l_zero * 2 + r_zero, r_zero * 2 - l_zero)


def solution(name):
    conv = [up_down(ch) for ch in name]
    return sum(conv) + move(conv[1:])


def main():
    assert solution("AAZAA") == 3
    assert solution("AAAZA") == 3
    assert solution("JAN") == 23
    assert solution("JEROEN") == 56
    assert solution("AAAAA") == 0
    assert solution("ABAAAAAAAAAAB")


if __name__ == '__main__':
    main()

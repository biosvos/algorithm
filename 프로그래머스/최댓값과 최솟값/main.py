def solution(s):
    arr = sorted([int(d) for d in s.split()])
    return f"{arr[0]} {arr[-1]}"


def main():
    assert solution("1 2 3 4") == "1 4"
    assert solution("-1 -2 -3 -4") == "-4 -1"
    assert solution("-1 -1") == "-1 -1"


if __name__ == '__main__':
    main()

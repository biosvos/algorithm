def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))


def main():
    assert solution(["sun", "bed", "car"], 1) == ["car", "bed", "sun"]
    assert solution(["abce", "abcd", "cdx"], 2) == ["abcd", "abce", "cdx"]


if __name__ == '__main__':
    main()

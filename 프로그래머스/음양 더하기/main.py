def solution(absolutes, signs):
    return sum([n if s else -n for n, s in zip(absolutes, signs)])


def main():
    assert solution([4, 7, 12], [True, False, True]) == 9


if __name__ == '__main__':
    main()

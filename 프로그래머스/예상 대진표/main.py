def solution(n, a, b):
    a -= 1
    b -= 1
    cnt = 0
    while a != b:
        a //= 2
        b //= 2
        cnt += 1

    return cnt


def main():
    assert solution(8, 4, 7) == 3


if __name__ == '__main__':
    main()

def solution(price, money, count):
    return max((((1 + count) * count / 2) * price) - money, 0)


def main():
    assert solution(3, 20, 4) == 10


if __name__ == '__main__':
    main()

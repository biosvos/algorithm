def solution(n):
    arr = []
    while n > 0:
        n, m = divmod(n - 1, 3)
        arr.append(m)
    arr.reverse()
    conv = {0: '1', 1: '2', 2: '4'}
    return ''.join(conv[n] for n in arr)


def main():
    print(solution(1))  # == "1"
    print(solution(2))  # == "2"
    print(solution(3))  # == "4"
    print(solution(4))  # == "11"
    print(solution(5))  # == "12"
    print(solution(6))  # == "14"
    print(solution(7))  # == "21"
    print(solution(8))  # == "22"
    print(solution(9))  # == "24"
    print(solution(10))  # == "41"
    print(solution(11))  # == "42"
    print(solution(12))  # == "44"
    print(solution(13))  # == "111"


if __name__ == '__main__':
    main()

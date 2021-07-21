def solution(seoul):
    i = seoul.index("Kim")
    return f"김서방은 {i}에 있다"


def main():
    print(solution(["Jane", "Kim"]))


if __name__ == '__main__':
    main()

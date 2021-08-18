def solution(n):
    return int(''.join(sorted(list(str(n)), reverse=True)))


def main():
    assert solution(118372) == 873211


if __name__ == '__main__':
    main()

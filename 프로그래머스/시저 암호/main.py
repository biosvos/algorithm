def solution(s, n):
    answer = ""
    for ch in s:
        if ch.isalpha():
            if ch.islower():
                ch = chr((ord(ch) - ord('a') + n) % 26 + ord('a'))
            else:
                ch = chr((ord(ch) - ord('A') + n) % 26 + ord('A'))
        answer += ch

    return answer


def main():
    print(solution("AB", 1))
    print(solution("z", 1))
    print(solution("a B z", 4))


if __name__ == '__main__':
    main()

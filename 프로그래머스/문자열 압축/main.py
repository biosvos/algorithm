def window_iter(s: str, interval: int):
    sz = len(s)
    start = 0
    while (start + interval) <= sz:
        yield s[start:start + interval]
        start += interval

    if start < sz:
        yield s[start:]


def solution(s):
    sz = len(s)
    answer = sz
    for window in range(1, sz // 2 + 1):
        it = window_iter(s, window)
        same_cnt = 0
        compress = ""
        prev = next(it)
        for cur in it:
            if prev == cur:
                same_cnt += 1
            else:
                if same_cnt > 0:
                    compress += f"{same_cnt + 1}"
                compress += prev
                same_cnt = 0
            prev = cur

        if same_cnt > 0:
            compress += f"{same_cnt + 1}"
        compress += prev
        answer = min(answer, len(compress))
    return answer


def main():
    assert solution("aabbaccc") == 7
    assert solution("ababcdcdababcdcd") == 9
    assert solution("abcabcdede") == 8
    assert solution("abcabcabcabcdededededede") == 14
    assert solution("xababcdcdababcdcd") == 17


if __name__ == '__main__':
    main()

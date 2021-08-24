def jaccard_string_iter(s: str):
    prev = ""
    for ch in s:
        if not ch.isalpha():
            prev = ""
            continue

        if prev != "":
            yield (prev + ch).lower()

        prev = ch


def solution(str1, str2):
    jaccard1 = sorted(list(jaccard_string_iter(str1)))
    jaccard2 = sorted(list(jaccard_string_iter(str2)))

    total_len = len(jaccard1) + len(jaccard2)
    if total_len == 0:
        return 65536

    same_cnt = 0
    while jaccard1 and jaccard2:
        if jaccard1[0] > jaccard2[0]:
            jaccard2.pop(0)
        elif jaccard1[0] < jaccard2[0]:
            jaccard1.pop(0)
        else:
            same_cnt += 1
            jaccard1.pop(0)
            jaccard2.pop(0)

    return int(same_cnt / (total_len - same_cnt) * 65536)


def main():
    assert solution("FRANCE", "french") == 16384
    assert solution("handshake", "shake hands") == 65536
    assert solution("aa1+aa2", "AAAA12") == 43690
    assert solution("E=M*C^2", "e=m*c^2") == 65536


if __name__ == '__main__':
    main()

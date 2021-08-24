def step01(s: str) -> str:
    return s.lower()


def step02(s: str) -> str:
    ret = ""
    for c in s:
        if c.isalnum():
            ret += c
        elif c in ['-', '_', '.']:
            ret += c

    return ret


def step03(s: str) -> str:
    ret = ""
    cont = False
    for c in s:
        if c == ".":
            if not cont:
                ret += c
            cont = True
        else:
            ret += c
            cont = False
    return ret


def step04(s: str) -> str:
    while len(s) > 0:
        if s[0] == ".":
            s = s[1:]
        elif s[-1] == ".":
            s = s[:-1]
        else:
            break

    return s


def step05(s: str) -> str:
    if s == "":
        return "a"

    return s


def step06(s: str) -> str:
    return s[:15]


def step07(s: str) -> str:
    remain = 3 - len(s)
    return s + s[-1] * remain


def pipeline(data, *fns):
    for fn in fns:
        data = fn(data)

    return data


def solution(new_id):
    return pipeline(new_id, step01, step02, step03, step04, step05, step06, step04, step07)


def main():
    assert solution("...!@BaT#*..y.abcdefghijklm") == "bat.y.abcdefghi"
    assert solution("z-+.^.") == "z--"
    assert solution("=.=") == "aaa"
    assert solution("123_.def") == "123_.def"
    assert solution("abcdefghijklmn.p") == "abcdefghijklmn"


if __name__ == '__main__':
    main()

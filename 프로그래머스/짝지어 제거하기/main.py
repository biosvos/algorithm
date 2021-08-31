def solution(s):
    st = []
    for ch in s:
        if st[-1:] == [ch]:
            st.pop()
        else:
            st.append(ch)

    return 0 if st else 1


def main():
    assert solution("baabaa") == 1
    assert solution("cdcd") == 0


if __name__ == '__main__':
    main()

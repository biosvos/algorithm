def solution(record):
    answer = []
    users = {}

    for r in record:
        st = r.split()
        if st[0] == "Enter":
            users[st[1]] = st[2]
        elif st[0] == "Change":
            users[st[1]] = st[2]

    for r in record:
        st = r.split()
        if st[0] == "Enter":
            answer.append(f"{users[st[1]]}님이 들어왔습니다.")
        elif st[0] == "Leave":
            answer.append(f"{users[st[1]]}님이 나갔습니다.")

    return answer


def main():
    assert solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo",
                     "Change uid4567 Ryan"]) == ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.",
                                                 "Prodo님이 들어왔습니다."]


if __name__ == '__main__':
    main()

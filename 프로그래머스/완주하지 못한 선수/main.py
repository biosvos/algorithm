def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append(None)
    for x, y in zip(participant, completion):
        if x != y:
            return x

    return None


def main():
    assert solution(["leo", "kiki", "eden"], ["eden", "kiki"]) == "leo"
    assert solution(["marina", "josipa", "nikola", "vinko", "filipa"],
                    ["josipa", "filipa", "marina", "nikola"]) == "vinko"
    assert solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]) == "mislav"


if __name__ == '__main__':
    main()

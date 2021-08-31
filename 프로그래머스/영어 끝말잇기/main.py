def solution(n, words):
    turn = failed_turn(words)
    if turn < 0:
        return [0, 0]
    d, m = divmod(turn, n)
    return [m + 1, d + 1]


def failed_turn(words):
    prev_last = words[0][0]
    word_set = set()
    for idx, word in enumerate(words):
        if word[0] != prev_last:
            return idx
        if word in word_set:
            return idx

        word_set.add(word)
        prev_last = word[-1]

    return -1


def main():
    assert solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]) == [3, 3]
    assert solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish",
                        "hang", "gather", "refer", "reference", "estimate", "executive"]) == [0, 0]
    assert solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]) == [1, 3]


if __name__ == '__main__':
    main()

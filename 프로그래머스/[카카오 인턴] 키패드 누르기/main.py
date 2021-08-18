def manhattan(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))


def solution(numbers, hand):
    table = [(i, j) for j in range(4) for i in range(3)]

    left = table[9]
    right = table[11]
    answer = ''
    for n in numbers:
        if n == 0:
            n = 10
        else:
            n -= 1
        touch = table[n]

        if n in [0, 3, 6]:
            left = touch
            answer += 'L'
        elif n in [2, 5, 8]:
            right = touch
            answer += 'R'
        else:
            ld = manhattan(left, touch)
            rd = manhattan(right, touch)
            if ld < rd:
                left = touch
                answer += 'L'
            elif ld > rd:
                right = touch
                answer += 'R'
            if ld == rd:
                if hand == "left":
                    left = touch
                    answer += 'L'
                else:
                    right = touch
                    answer += 'R'

    return answer


def main():
    assert solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL"
    assert solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") == "LRLLRRLLLRR"
    assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") == "LLRLLRLLRL"


if __name__ == '__main__':
    main()

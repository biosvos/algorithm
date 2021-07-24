def solution(numbers, hand):
    # * --> 10
    # 0 --> 11
    # # --> 12
    answer = []
    LEFT = 0
    RIGHT = 1

    choice = [
        None,
        LEFT, None, RIGHT,
        LEFT, None, RIGHT,
        LEFT, None, RIGHT,
        LEFT, None, RIGHT
    ]

    left_num = 10
    right_num = 12
    for n in numbers:
        if choice[n] == LEFT:
            left_num = n
            answer.append('L')
        elif choice[n] == RIGHT:
            right_num = n
            answer.append('R')
        else:
            if n == 0:
                n = 11

            l_hand = left_num
            r_hand = right_num
            l_dist = 0
            r_dist = 0

            if choice[left_num] is not None:
                l_hand += 1
                l_dist = 3

            if choice[right_num] is not None:
                r_hand -= 1
                r_dist = 3

            l_dist += abs(l_hand - n)
            r_dist += abs(r_hand - n)

            if l_dist < r_dist:
                left_num = n
                answer.append('L')
            elif l_dist > r_dist:
                right_num = n
                answer.append('R')
            else:
                if hand == "left":
                    left_num = n
                    answer.append('L')
                else:
                    right_num = n
                    answer.append('R')

    return ''.join(answer)


def main():
    assert solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL"
    assert solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") == "LRLLRRLLLRR"
    assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") == "LLRLLRLLRL"


if __name__ == '__main__':
    main()

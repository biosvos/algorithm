def digit_start_number(digit, base=10):
    start = 0
    if digit > 1:
        start = base ** (digit - 1)
    return start


def digit_diff(digit, base=10):
    return digit_start_number(digit + 1, base=base) - digit_start_number(digit, base=base)


def num2str(n):
    if n < 10:
        return str(n)
    return chr(ord('A') + n - 10)


# 너무 어렵게 생각했네??


def solution(base, times, members, turn):
    """
    :param base: 진법, ex> 10진법, 16진법
    :param times: 차례의 횟수
    :param members: 멤버 수
    :param turn: 차례, 멤버들 중 자신의 차례, 1부터 시작
    :return:
    """
    answer = ''
    turn -= 1  # 0부터 시작으로 변경

    for i in range(times):
        game_turn = members * i + turn

        start = 0
        end = digit_start_number(2, base=base)
        digit = 1

        while True:
            if game_turn < end:
                break
            digit += 1
            diff = digit_diff(digit, base=base) * digit
            start = end
            end = start + diff

        # print(f"게임 턴: {game_turn} 자릿수: {digit}, digit 턴: {start} ~ {end}")
        number = digit_start_number(digit, base=base) + ((game_turn - start) // digit)
        number_cnt = digit - ((game_turn - start) % digit)
        # print(f"숫자: {number}, 번째: {number_cnt}")
        n = number
        for j in range(number_cnt - 1):
            n //= base

        answer += num2str(n % base)

    return answer


def main():
    assert solution(2, 4, 2, 1) == "0111"
    assert solution(16, 16, 2, 1) == "02468ACE11111111"
    assert solution(16, 16, 2, 2) == "13579BDF01234567"


if __name__ == '__main__':
    main()

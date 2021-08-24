import itertools
import re


def calc(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b


def solution(expression):
    num_regex = re.compile('[0-9]+')
    op_regex = re.compile('([+-/*])')

    nums = [int(n) for n in num_regex.findall(expression)]
    ops = op_regex.findall(expression)
    op_set = set(ops)
    op_len = len(set(ops))
    answer = 0

    for op_order in itertools.permutations(op_set, op_len):
        nums_temp = nums.copy()
        ops_temp = ops.copy()
        for op in op_order:
            while op in ops_temp:
                idx = ops_temp.index(op)
                del ops_temp[idx]
                nums_temp[idx] = calc(nums_temp[idx], op, nums_temp[idx + 1])
                del nums_temp[idx + 1]

        answer = max(answer, abs(nums_temp[0]))

    return answer


def main():
    assert solution("100-200*300-500+20") == 60420
    assert solution("50*6-3*2") == 300


if __name__ == '__main__':
    main()

def solution(board, moves):
    n = len(board)
    r_board = []
    for i in range(n):
        arr = []
        for j in range(n):
            if board[j][i] > 0:
                arr.append(board[j][i])
        r_board.append(arr)

    ret = 0
    items = []
    for pick in moves:
        pick -= 1
        if len(r_board[pick]) == 0:
            continue

        item = r_board[pick].pop(0)
        if items[-1:] == [item]:
            ret += 2
            items.pop()
        else:
            items.append(item)

    return ret


def main():
    assert solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
                    [1, 5, 3, 5, 1, 2, 1, 4]) == 4


if __name__ == '__main__':
    main()

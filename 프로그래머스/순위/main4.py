class Player:
    def __init__(self):
        self.win = set()
        self.lose = set()

    def is_rank_confirmed(self, total_player: int) -> bool:
        return len(self.win) + len(self.lose) == total_player - 1


def convert2players(n, results):
    players = [Player() for _ in range(n)]
    for item in results:
        players[item[0] - 1].win.add(item[1] - 1)
        players[item[1] - 1].lose.add(item[0] - 1)
    return players


def solution(n, results):
    players = convert2players(n, results)

    for i in range(n):
        for j in players[i].win:
            # "나한테 진 참가자"는 "나를 이긴 참가자"한테 진다.
            players[j].lose.update(players[i].lose)
        for j in players[i].lose:
            # "나를 이긴 참가자"는 "나한테 진 참가자"한테 이긴다.
            players[j].win.update(players[i].win)

    return sum([1 for player in players if player.is_rank_confirmed(n)])


def main():
    assert solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]) == 2
    assert solution(3, [[1, 2], [1, 3], [2, 3]]) == 3
    assert solution(3, [[1, 2], [2, 3]]) == 3


if __name__ == '__main__':
    main()

from enum import Enum, auto


class MatchStatus(Enum):
    UNKNOWN = auto()  # 자기 자신과의 싸움 결과는 알 수 없다.
    WIN = auto()
    LOSE = auto()


def inherit_lose(graph, parent_idx, child_idx):
    for i in range(len(graph)):
        if graph[parent_idx][i] == MatchStatus.LOSE:
            graph[child_idx][i] = MatchStatus.LOSE
            graph[i][child_idx] = MatchStatus.WIN


def inherit_win(graph, parent_idx, child_idx):
    for i in range(len(graph)):
        if graph[parent_idx][i] == MatchStatus.WIN:
            graph[child_idx][i] = MatchStatus.WIN
            graph[i][child_idx] = MatchStatus.LOSE


def solution(n, results):
    results = [[win - 1, lose - 1] for win, lose in results]

    # input to graph
    graph = input_to_graph(n, results)

    for i in range(n):
        for j in range(n):
            if graph[i][j] == MatchStatus.UNKNOWN:
                continue

            if graph[i][j] == MatchStatus.WIN:
                # "나한테 진 참가자"는 "나를 이긴 참가자"한테 진다.
                inherit_lose(graph, i, j)
            elif graph[i][j] == MatchStatus.LOSE:
                # "나를 이긴 참가자"는 "나한테 진 참가자"한테 이긴다.
                inherit_win(graph, i, j)

    ret = 0
    for g in graph:
        if g.count(MatchStatus.UNKNOWN) == 1:
            ret += 1

    return ret


def input_to_graph(n, results):
    graph = [[MatchStatus.UNKNOWN] * n for _ in range(n)]
    for item in results:
        graph[item[0]][item[1]] = MatchStatus.WIN
        graph[item[1]][item[0]] = MatchStatus.LOSE
    return graph


def main():
    assert solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]) == 2
    assert solution(3, [[1, 2], [1, 3], [2, 3]]) == 3
    assert solution(3, [[1, 2], [2, 3]]) == 3


if __name__ == '__main__':
    main()

# 승률 내림차순, 자신보다 무거운애 이긴 횟수 내림차순, 무거운애 내림차순, 번호 오름차순
# 안싸웠으면 0퍼 취급

def ratio(win, total):
    if total == 0:
        return 0
    return win / total


def solution(weights, head2head):
    arr = []
    for i, weight in enumerate(weights):
        win_cnt = 0
        rel_heavy_win_cnt = 0
        lose_cnt = 0
        for j, fight in enumerate(head2head[i]):
            if fight == 'W':
                win_cnt += 1
                if weight < weights[j]:
                    rel_heavy_win_cnt += 1
            elif fight == 'L':
                lose_cnt += 1
        arr.append([-ratio(win_cnt, (win_cnt + lose_cnt)), -rel_heavy_win_cnt, -weight, i + 1])
    arr.sort()
    return [a[3] for a in arr]


def main():
    assert solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"]) == [3, 4, 1, 2]
    assert solution([145, 92, 86], ["NLW", "WNL", "LWN"]) == [2, 3, 1]
    assert solution([60, 70, 60], ["NNN", "NNN", "NNN"]) == [2, 1, 3]


if __name__ == '__main__':
    main()

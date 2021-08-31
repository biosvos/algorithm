class Position:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def manhattan(a: Position, b: Position):
    return abs(a.x - b.x) + abs(a.y - b.y)


def middle(a: Position, b: Position):
    if a.x == b.x:
        return [Position(a.x, (a.y + b.y) // 2)]
    if a.y == b.y:
        return [Position((a.x + b.x) // 2, a.y)]

    return [Position(a.x, b.y), Position(b.x, a.y)]


def p_iter(place):
    for i, row in enumerate(place):
        for j, item in enumerate(row):
            if item != "P":
                continue
            yield Position(i, j)


def check_social_distancing(place):
    p_locations = []
    for cur in p_iter(place):
        for prev in p_locations:
            d = manhattan(prev, cur)
            if d > 2:
                continue
            if d == 1:
                return 0
            if d == 2:
                mid_list = middle(prev, cur)
                if any(place[mid.x][mid.y] != "X" for mid in mid_list):
                    return 0

        p_locations.append(cur)
    return 1


def solution(places):
    return [check_social_distancing(p) for p in places]


def main():
    assert solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                     ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                     ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]) == [1, 0, 1, 1, 1]


if __name__ == '__main__':
    main()

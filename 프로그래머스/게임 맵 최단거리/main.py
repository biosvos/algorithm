class Map:
    __arr: list[list[int]]

    def __init__(self, m):
        self.__arr = m

    def set(self, x: int, y: int, item: int):
        if x < 0 or y < 0:
            raise ValueError("맵 범위를 벗어남")
        if item < 1:
            raise ValueError("item 은 1 이상이여야 함")
        if self.__arr[x][y] != 1:
            raise ValueError("update 불가")
        self.__arr[x][y] = item + 1

    def get(self, x: int, y: int) -> int:
        if x < 0 or y < 0:
            raise ValueError("맵 범위를 벗어남")
        if self.__arr[x][y] < 2:
            raise ValueError("값이 없음")
        return self.__arr[x][y] - 1


def solution(maps):
    m = Map(maps)
    m.set(0, 0, 1)
    st = [(0, 0)]

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]

    while st:
        i, j = st.pop(0)
        try:
            item = m.get(i, j)
        except:
            continue

        for direction in directions:
            try:
                m.set(i + direction[0], j + direction[1], item + 1)
                st.append((i + direction[0], j + direction[1]))
            except:
                continue

    last = maps[-1][-1]
    if last == 1:
        return -1
    return last - 1


def main():
    assert solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]) == 11
    assert solution([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]) == 9
    assert solution([[1, 1, 1, 0, 1]]) == -1
    assert solution([[1, 1, 1, 1, 1]]) == 5
    assert solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]) == -1


if __name__ == '__main__':
    main()

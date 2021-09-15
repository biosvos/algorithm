LEFT = 1
RIGHT = 2
UP = 4
DOWN = 8


def next_pos(item, i, j, direction):
    if item == "S":
        if direction == LEFT:
            return i - 1, j
        elif direction == RIGHT:
            return i + 1, j
        elif direction == UP:
            return i, j - 1
        else:  # DOWN
            return i, j + 1
    elif item == "L":
        if direction == LEFT:
            return i, j-1
        elif direction == RIGHT:
            return i+1, j
        elif direction == UP:
            return
        else:  # DOWN
            return
    else:  # R
        pass


def solution(grid):
    visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    print(visited)
    for i, row in enumerate(grid):
        for j, item in enumerate(row):
            for direction in [LEFT, RIGHT, UP, DOWN]:
                # print(i, j, item)
                while not visited[i][j] & direction:
                    visited[i][j] |= direction
    print(visited)


def main():
    assert solution(["S"]) == [1, 1, 1, 1]
    assert solution(["SL", "LR"]) == [16]
    assert solution(["R", "R"]) == [4, 4]


if __name__ == '__main__':
    main()

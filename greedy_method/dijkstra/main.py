INF = 999


def get_min_vertex(dist, selected):
    min_vertex = -1
    min_dist = INF
    for v in range(len(dist)):
        if not selected[v] and dist[v] < min_dist:
            min_dist = dist[v]
            min_vertex = v

    return min_vertex


def shortest_path(vtx: list[str], adj: list[list[int]], start: int):
    v_len = len(vtx)
    dist = adj[start]
    dist[start] = 0
    path = [start] * v_len
    found = [False] * v_len
    found[start] = True

    for i in range(v_len):
        print(f"Step{i + 1}: {dist}")
        u = get_min_vertex(dist, found)
        found[u] = True

        for w in range(v_len):
            if dist[u] + adj[u][w] < dist[w]:
                dist[w] = dist[u] + adj[u][w]
                path[w] = u

    return path


def main():
    vtx = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    weight = [
        [0, 7, INF, INF, 3, 10, INF],
        [7, 0, 4, 10, 2, 6, INF],
        [INF, 4, 9, 2, INF, INF, INF],
        [INF, 10, 2, 0, 11, 9, 4],
        [3, 2, INF, 11, 0, 13, 5],
        [10, 6, INF, 9, 13, 0, INF],
        [INF, INF, INF, 4, 5, INF, 0]
    ]
    shortest_path(vtx, weight, 0)


if __name__ == '__main__':
    main()

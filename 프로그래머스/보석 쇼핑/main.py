class Scope(object):
    start_idx: int
    end_idx: int

    def __init__(self):
        self.start_idx = -1
        self.end_idx = -1

    def __repr__(self):
        return f"{self.start_idx} ~ {self.end_idx}"

    def __iter__(self):
        if self.start_idx < 0 and self.end_idx < 0:
            return iter(range(0))

        return iter(range(self.start_idx, self.end_idx + 1))

    def update(self, idx):
        if self.start_idx < 0 and self.end_idx < 0:
            self.start_idx = idx
            self.end_idx = idx
            return

        if idx < self.start_idx:
            self.start_idx = idx

        if self.end_idx < idx:
            self.end_idx = idx


def solution(gems):
    m = {}
    for idx, gem in enumerate(gems):
        r = m.get(gem, None)
        if r is None:
            m[gem] = []
        m[gem].append(idx)

    # 한개만 있는거 처리, 반드시 포함되어야 함
    one = [(k, v[0]) for k, v in m.items() if len(v) == 1]
    scope = Scope()
    for k, v in one:
        scope.update(v)
        del m[k]
    for idx in scope:
        if gems[idx] in m:
            del m[gems[idx]]

    changed = True
    while changed:
        changed = False
        # left side
        left = [(k, v[-1]) for k, v in m.items() if v[-1] < scope.start_idx]
        for k, v in left:
            changed = True
            scope.update(v)
            del m[k]
        for idx in scope:
            if gems[idx] in m:
                del m[gems[idx]]

        # right side
        right = [(k, v[0]) for k, v in m.items() if scope.end_idx < v[0]]
        for k, v in right:
            changed = True
            scope.update(v)
            del m[k]
        for idx in scope:
            if gems[idx] in m:
                del m[gems[idx]]

    if not m:
        return [scope.start_idx + 1, scope.end_idx + 1]

    left = len(gems)
    right = 0
    for k, v in m.items():
        l_ret = 0
        r_ret = 0
        for idx in v:
            if idx < scope.start_idx:
                l_ret = idx
            elif scope.end_idx < idx:
                r_ret = idx
                break
        left = min(left, l_ret)
        right = max(right, r_ret)

    if (scope.end_idx - left) <= (right - scope.start_idx):
        return [left + 1, scope.end_idx + 1]
    return [scope.start_idx + 1, right + 1]


def main():
    assert solution(["A", "B", "C", "A", "A"]) == [1, 3]
    assert solution(["A", "B", "C", "B", "A"]) == [1, 3]
    assert solution(["A", "B", "C", "A", "B"]) == [1, 3]
    assert solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]) == [3, 7]
    assert solution(["XYZ", "XYZ", "XYZ"]) == [1, 1]
    assert solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]) == [1, 5]
    assert solution(["AA", "AB", "AC", "AA", "AC"]) == [1, 3]


if __name__ == '__main__':
    main()

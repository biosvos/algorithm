import heapq


class ImmigrationInspector:
    __waiting_time: int
    __work_time: int

    def __init__(self, work_time):
        self.__work_time = work_time
        self.__waiting_time = 0

    def __repr__(self):
        return f"{self.__waiting_time}"

    @property
    def waiting_time(self):
        return self.__waiting_time

    @property
    def expect_time(self):
        return self.__waiting_time + self.__work_time

    def selected(self):
        self.__waiting_time += self.__work_time


def solution(n, times):
    inspectors = [ImmigrationInspector(time) for time in times]

    hq = [(inspector.expect_time, inspector) for inspector in inspectors]
    heapq.heapify(hq)

    for i in range(n):
        item = heapq.heappop(hq)
        inspector = item[1]
        inspector.selected()
        heapq.heappush(hq, (inspector.expect_time, inspector))

    return max(inspectors, key=lambda x: x.waiting_time).waiting_time


def main():
    assert solution(6, [7, 10]) == 28
    assert solution(6, [1, 9]) == 6


if __name__ == '__main__':
    main()

import heapq


def mix_scoville(a: int, b: int) -> int:
    if a > b:
        a, b = b, a
    return a + b * 2


def solution(scoville: list, k: int) -> int:
    heapq.heapify(scoville)

    ret = 0
    while a := heapq.heappop(scoville):
        if a >= k:
            heapq.heappush(scoville, a)
            return ret

        if len(scoville) == 0:
            return -1

        b = heapq.heappop(scoville)
        heapq.heappush(scoville, mix_scoville(a, b))
        ret += 1

    return -1


def main():
    assert solution([1, 2, 3, 9, 10, 12], 7) == 2


if __name__ == '__main__':
    main()

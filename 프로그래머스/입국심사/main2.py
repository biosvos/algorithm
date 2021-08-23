import heapq


def solution(n, times):
    # 기대 대기시간, 일 처리 시간
    # 기대 대기시간은 입국자를 기준으로 줄 기다리는 시간 + 입국심사관의 일 처리 시간을 뜻함
    inspectors = [(time, time) for time in times]
    heapq.heapify(inspectors)

    for i in range(n):
        item = heapq.heappop(inspectors)
        heapq.heappush(inspectors, (item[0] + item[1], item[1]))

    return max(x[0] - x[1] for x in inspectors)


def main():
    assert solution(6, [7, 10]) == 28
    assert solution(6, [1, 9]) == 6


if __name__ == '__main__':
    main()

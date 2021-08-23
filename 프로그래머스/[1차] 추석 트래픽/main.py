import datetime

TIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"


def parse_line(s: str):
    s = s.split()
    date = datetime.datetime.strptime(s[0] + " " + s[1], TIME_FORMAT)
    try:
        delta = datetime.datetime.strptime(s[2], "%S.%fs")
    except ValueError:
        delta = datetime.datetime.strptime(s[2], "%Ss")

    delta = datetime.timedelta(seconds=delta.second, microseconds=delta.microsecond - 1000)
    return date, delta


def filtering(arr: list, fn):
    del_item = []
    for idx, item in enumerate(arr):
        if fn(item):
            del_item.insert(0, idx)

    for d in del_item:
        del arr[d]


def solution(lines):
    lines = [parse_line(line) for line in lines]
    window_1sec = []
    max_cnt = 0
    for rec in reversed(lines):
        window_1sec.append(rec[0] - rec[1])  # window 에서 나가야 하는 시간 추가

        # 추가한 거를 포함한 이후 시간
        pivot_time = rec[0] + datetime.timedelta(seconds=1, microseconds=-1000)
        filtering(window_1sec, lambda x: pivot_time < x)
        max_cnt = max(max_cnt, len(window_1sec))

    return max_cnt  # 최소 1 ~ 최대 라인 갯수


def main():
    assert solution([
        "2016-09-15 01:00:04.002 2.0s",
        "2016-09-15 01:00:07.000 2s"
    ]) == 2
    assert solution([
        "2016-09-15 01:00:04.001 2.0s",
        "2016-09-15 01:00:07.000 2s"
    ]) == 1
    assert solution([
        "2016-09-15 20:59:57.421 0.351s",
        "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s",
        "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s",
        "2016-09-15 21:00:00.748 2.31s",
        "2016-09-15 21:00:00.966 0.381s",
        "2016-09-15 21:00:02.066 2.62s"
    ]) == 7
    assert solution([
        "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s",
        "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s",
        "2016-09-15 21:00:00.748 2.31s",
    ]) == 7


if __name__ == '__main__':
    main()

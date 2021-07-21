def solution(max_stage, stages):
    count_stage = [0] * max_stage
    size = len(stages)

    for stage in stages:
        if stage <= max_stage:
            count_stage[stage - 1] += 1

    stage_failure = [0.0] * max_stage
    for calc_stage in range(max_stage):
        stage_failure[calc_stage] = count_stage[calc_stage] / size
        size -= count_stage[calc_stage]
        if size == 0:
            break

    failure_with_index = enumerate(stage_failure, start=1)
    sorted_failure_with_index = sorted(failure_with_index, key=lambda x: x[1], reverse=True)

    return [x[0] for x in sorted_failure_with_index]


def main():
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
    print(solution(4, [4, 4, 4, 4, 4]))


if __name__ == '__main__':
    main()

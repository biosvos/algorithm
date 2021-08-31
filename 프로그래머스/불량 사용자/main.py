import re


# def rec(ban_match, idx, ret: list):
#     if len(ban_match) == idx:
#         if len(set(ret)) == len(ret)
#         print(ret)
#         return 1 if len(set(ret)) == len(ret) else 0
#
#     n = 0
#     for ban in ban_match[idx]:
#         ret.append(ban)
#         n += rec(ban_match, idx + 1, ret)
#         ret.pop()
#
#     return n


def solution(user_id, banned_id):
    ban_match = []
    for ban in banned_id:
        ban = ban.replace("*", ".")
        p = re.compile(f"^{ban}$")
        users = [user for user in user_id if p.match(user)]
        ban_match.append(users)

    print(ban_match)
    ban_set = set()
    for bans in ban_match:
        for ban in bans:
            ban_set.add(ban)
    print(ban_set)
    # nums = [len(v) for v in ban_match]
    # ret = 1
    # for n in nums:
    #     ret *= n

    # result = rec(ban_match, 0, [])
    # print(result)
    # return result


def main():
    assert solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]) == 2
    assert solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]) == 3
    assert solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]) == 2


if __name__ == '__main__':
    main()

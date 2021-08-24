import itertools


def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return True


def solution2(phone_book):
    for a, b in itertools.combinations(phone_book, 2):
        if len(a) < len(b):
            a, b = b, a
        if a.startswith(b):
            return False

    return True


def main():
    assert not solution(["119", "97674223", "1195524421"])
    assert solution(["123", "456", "789"])
    assert not solution(["12", "123", "1235", "567", "88"])


if __name__ == '__main__':
    main()

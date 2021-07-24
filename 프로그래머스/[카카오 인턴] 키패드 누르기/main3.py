class Phone:
    @staticmethod
    def row(button):
        return (button - 1) // 3

    @staticmethod
    def col(button):
        return (button - 1) % 3

    @staticmethod
    def distance(src, dst):
        return abs(Phone.row(src) - Phone.row(dst)) + abs(Phone.col(src) - Phone.col(dst))


class Hand:
    __location: int

    def __init__(self, location):
        self.__location = location

    @abstractmethod
    def press(self, item):
        pass

    @abstractmethod
    def distance(self, item):
        pass


INF = 888


class LeftHand(Hand):
    def press(self, item):
        if item in Phone.RIGHT_SIDE:
            raise ValueError

        self.__location = item

    def distance(self, item):
        if item in Phone.RIGHT_SIDE:
            return INF
        elif item in Phone.LEFT_SIDE:
            return 0

        loc = self.__location
        dist = 0
        if loc in Phone.LEFT_SIDE:
            loc += 1
            dist = 3
        dist += abs(loc - item)
        return dist


class RightHand(Hand):
    def press(self, item):
        if item in Phone.LEFT_SIDE:
            raise ValueError

        self.__location = item

    def distance(self, item):
        if item in Phone.LEFT_SIDE:
            return INF
        elif item in Phone.RIGHT_SIDE:
            return 0

        loc = self.__location
        dist = 0
        if loc in Phone.RIGHT_SIDE:
            loc -= 1
            dist = 3
        dist += abs(loc - item)
        return dist


def solution(numbers, hand):
    pass


def main():
    assert Phone.row(1) == 0
    assert Phone.row(2) == 0
    assert Phone.row(3) == 0
    assert Phone.row(4) == 1
    assert Phone.row(5) == 1
    assert Phone.row(6) == 1
    assert Phone.row(7) == 2
    assert Phone.row(8) == 2
    assert Phone.row(9) == 2
    assert Phone.row(10) == 3
    assert Phone.row(11) == 3
    assert Phone.row(12) == 3

    assert Phone.col(1) == 0
    assert Phone.col(4) == 0
    assert Phone.col(7) == 0
    assert Phone.col(10) == 0
    assert Phone.col(2) == 1
    assert Phone.col(5) == 1
    assert Phone.col(8) == 1
    assert Phone.col(11) == 1
    assert Phone.col(3) == 2
    assert Phone.col(6) == 2
    assert Phone.col(9) == 2
    assert Phone.col(12) == 2


#    assert solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL"
#    assert solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") == "LRLLRRLLLRR"
#    assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") == "LLRLLRLLRL"


if __name__ == '__main__':
    main()

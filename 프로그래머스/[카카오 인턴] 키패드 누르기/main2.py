# 심심
from abc import *


class Phone:
    @staticmethod
    def row(button):
        return (button - 1) / 3

    @staticmethod
    def col(button):
        return (button - 1) % 3

    @staticmethod
    def button_distance(src, dst):
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


class Person:
    left: LeftHand
    right: RightHand
    default: Hand

    def __init__(self, default):
        self.left = LeftHand(10)
        self.right = RightHand(12)
        if default == "left":
            self.default = self.left
        else:  # "right"
            self.default = self.right

    def click(self, n):
        ref = self.default

        if n == 0:
            n = 11

        ld = self.left.distance(n)
        rd = self.right.distance(n)

        if ld < rd:
            ref = self.left
        elif ld > rd:
            ref = self.right

        ref.press(n)
        return "L" if ref == self.left else "R"


def solution(numbers, hand):
    answer = ""
    person = Person(hand)
    for n in numbers:
        answer += person.click(n)
    return answer


def main():
    assert solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL"
    assert solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") == "LRLLRRLLLRR"
    assert solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") == "LLRLLRLLRL"


if __name__ == '__main__':
    main()

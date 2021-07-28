class HuffmanTree:
    __freq: int
    __ch: str
    __left
    __right

    def __init__(self, freq: int, ch: str = ''):
        self.__freq = freq
        self.__ch = ch
        self.__left = None
        self.__right = None

    @property
    def freq(self):
        return self.__freq

    @property
    def ch(self):
        return self.__ch

    @staticmethod
    def merge(a, b):
        return 1

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    @left.setter
    def left(self, v):
        self.__left = v

    @right.setter
    def right(self, v):
        self.__right = v


def main():
    pass


if __name__ == '__main__':
    main()

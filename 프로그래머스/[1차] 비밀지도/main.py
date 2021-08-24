def solution(n, arr1, arr2):
    return ["{0:b}".format(x | y).replace("1", "#").replace("0", " ").rjust(n) for x, y in
            zip(arr1, arr2)]


def main():
    assert solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]) == ["#####", "# # #", "### #", "# ##", "#####"]
    assert solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]) == ["######", "### #", "## ##", " #### ",
                                                                               " #####", "### # "]


if __name__ == '__main__':
    main()

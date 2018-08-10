# coding=utf-8

# author: xwolf
# origin: https://www.lintcode.com/problem/a-b-problem/description
# date: 2018-08-10 16:25

class aPlusb:

    def __init__(self):
        pass

    def plus(self, a, b):
        """
        :param a:
        :param b:
        :return: a和b的和
        """
        c = a + b
        if c > 1 << 31:
            return 1 << 31
        if c < ((1 >> 31) - 1):
            return (1 >> 31) - 1
        return c


if __name__ == '__main__':
    two = aPlusb()
    a = 32
    b = 32
    c = two.plus(a, b)
    print(c)

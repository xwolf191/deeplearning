# coding=utf-8

# author: xwolf
# origin: https://leetcode.com/problems/powx-n/description/
class pow:

    def __init__(self):
        pass

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n == 0:
            return 1.0
        if n < 0:
            n = -n
            x = 1 / x
        return self.myPow(x * x, n // 2) if n % 2 == 0 else x * self.myPow(x * x, n // 2)


if __name__ == '__main__':
    p = pow()
    a = p.myPow(2.00000, 10)
    print(a)

import numpy as np

def basic():
    """
     行列式基础
     二阶行列式、三阶行列式
    :return:
    """
    a = np.array([[2, 3], [4, 9]])
    b = np.linalg.det(a)
    print(b)
    # 三阶行列式
    c = np.array([[2, 3, 6], [4, 9, 6],[2, 4, 5]])
    d = np.linalg.det(c)
    print(d)
    # 行列式转置
    e = c.transpose()
    print(e)

basic()
# coding=UTF-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


def histogram():
    """
     绘制直方图
    :return:
    """
    myfont = fm.FontProperties(fname="C:\Windows\Fonts\simsun.ttc")
    np.random.seed(19680801)
    mu = 200
    sigma = 25
    x = np.random.normal(mu, sigma, size=100)
    fig, (ax1) = plt.subplots(ncols=1, figsize=(8, 4))
    bins = [100, 150, 180, 195, 205, 220, 250, 300]
    ax1.hist(x, bins, density=True, histtype='bar', rwidth=0.8)
    ax1.set_label("ABC")
    ax1.set_title('XX公司2017年度各月份营业额', fontproperties=myfont)
    fig.tight_layout()
    plt.show()


histogram()

import re


def match(phone):
    """
      验证合法手机号
     :param phone: 手机号
     :return:
     """
    a = re.match('^(13|14|15|16|17|18|19)\d{9}$', phone)
    b = a is not None
    print(a)
    print(b)
    if b:
        print(a.group())


def search(phone):
    """
      验证合法手机号
     :param phone: 手机号
     :return:
     """
    a = re.search('^(13|14|15|16|17|18|19)\d{9}$', phone)
    b = a is not None
    print(a)
    print(b)
    if b:
        print(a.group())

search('13070000000')

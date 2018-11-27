from functools import reduce
import operator

def fac(n):
    return reduce(operator.mul, range(1, n+1), 1)
                            # 阶乘n!的定义
                            # reduce与operator.mul结合
def perm(n, k):
    return reduce(operator.mul, range(n-k+1, n+1), 1)
                            # 排列数的定义
def comb(n, k):
    return perm(n, k)//fac(k)

def test():
    print('{}!={}'.format(5, fac(5)))
    print('A_{}^{}={}'.format(5, 2, perm(5, 2)))
    print('C_{}^{}={}'.format(5, 2, comb(5, 2)))
    print(1-perm(365, 23)/(365**23))
    print(1-perm(365, 50)/(365**50))
if __name__ == '__main__':
    test()
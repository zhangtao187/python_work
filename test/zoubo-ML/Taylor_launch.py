def calc_sin_small(x):
    x2=-x**2
    t=x
    f=1
    sum=0
    for i in range(10):
        sum+=t/f
        t*=x2
        f*=((2*i+2)*(2*i+3))
        return sum

def calc_sin(x):

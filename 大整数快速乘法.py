'''
大整数快速乘法
'''
import math
def divideMultiply(x,y,n):
    if n>min([len(str(x)),len(str(y))]):        #判断给定的n是不是最小位数
        return 0
    if (x==0)|(y==0):
        return 0
    sign=int((x/abs(x))*(y/abs(y))) #确定最终符号
    x,y=abs(x),abs(y)               #变为正整数
    if n==1:
        return sign*x*y
    else:                                       #分为几段并递归计算
        A=int(x/math.pow(10,int(n/2)))
        B=x-A*math.pow(10,int(n/2))
        C=int(y/math.pow(10,int(n/2)))
        D=y-C*math.pow(10,int(n/2))
        AC=divideMultiply(A,C,int(n/2))
        BD=divideMultiply(B,D,int(n/2))
        ABDC=divideMultiply((A-B),(D-C),int(n/2))+AC+BD
    return int(sign*(AC * math.pow(10,n)+ABDC*pow(10,int(n/2))+ BD))
divideMultiply(12345678910,123456789,9)
#Out:15240814529753620480

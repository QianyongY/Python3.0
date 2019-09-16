# -*-coding:utf-8-*-

a = 21
b = 10
c = 0


'''
    Python算术运算符
'''
c = a + b
print("1 - c 的值为：", c)

c = a - b
print("2 - c 的值为：", c)

c = a * b
print("3 - c 的值为：", c)

c = a / b
print("4 - c 的值为：", c)

c = a % b
print("5 取余  - c 的值为：", c)

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print("6 幂 - 返回x的y次幂 - c 的值为：", c)

a = 10
b = 5
c = a // b
print("7 取模即为取整除 - 向下取接近除数的整数 - c 的值为：", c)

'''
    赋值运算符
'''

a = 21
b = 10
c = 0

c = a + b
print("2.1	简单的赋值运算符 c = a + b 将 a + b 的运算结果赋值为 c    - c 的值为：", c)

c += a
print("2.2	加法赋值运算符	c += a 等效于 c = c + a      - c 的值为：", c)

c *= a
print("2.3  乘法赋值运算符 - c 的值为：", c)

c /= a
print("2.4  除法赋值运算符- c 的值为：", c)

c = 2
c %= a
print("2.5 	取余赋值运算符 - c 的值为：", c)

c **= a
print("2.6  幂赋值运算符- c 的值为：", c)

c //= a
print("2.7  取整除赋值运算符- c 的值为：", c)


'''
    比较运算符
'''

a = 21
b = 10
c = 0

if (a == b):
    print("1 - a 等于 b")
else:
    print("1 - a 不等于 b")

if (a != b):
    print("2 - a 不等于 b")
else:
    print("2 - a 等于 b")

if (a < b):
    print("3 - a 小于 b")
else:
    print("3 - a 大于等于 b")

if (a > b):
    print("4 - a 大于 b")
else:
    print("4 - a 小于等于 b")

# 修改变量 a 和 b 的值
a = 5;
b = 20;
if (a <= b):
    print("5 - a 小于等于 b")
else:
    print("5 - a 大于  b")

if (b >= a):
    print("6 - b 大于等于 a")
else:
    print("6 - b 小于 a")


'''
    逻辑运算符
'''
a = 10
b = 20

if (a and b):#and两个条件都为真才为真
    print("1 - 变量 a 和 b 都为 true")
else:
    print("1 - 变量 a 和 b 有一个不为 true")

if (a or b):#至少一个条件为真即为真
    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("2 - 变量 a 和 b 都不为 true")

# 修改变量 a 的值
a = 0
if (a and b):
    print("3 - 变量 a 和 b 都为 true")
else:
    print("3 - 变量 a 和 b 有一个不为 true")

if (a or b):
    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
    print("4 - 变量 a 和 b 都不为 true")

if not (a and b):
    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
    print("5 - 变量 a 和 b 都为 true")


str = '' #空字符串 返回bool false
str = [] #空列表 返回bool false
str = () #空列表 返回bool false
str = {} #空列表 返回bool false
num =0   #0 返回bool false
print(bool(num))


'''
    位运算符
'''

a=4
b=2
'''
    0000 0100 4
    0000 0010 2
    0000 0000 0

'''


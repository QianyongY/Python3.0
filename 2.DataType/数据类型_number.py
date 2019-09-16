# -*-coding:utf-8-*-

'''

    int

'''

numberA = 1
print(type(numberA))
#type()是python中一个用来查看数据类型的函数

'''

    布尔类型
    对TRUE 不为0的数
    错FALSE  0

'''

boolA = True
print(type(boolA))


'''

    字符串
    单引号或者双引号

'''

student1 = '刘德华'
student2 = "黎明"
num = '1'
bool2 ='true'

#单引号的都是字符串

print(type(student1))
print(type(student2))
print(type(num))
print(type(bool2))


str1 ='"你好"'
str2 = "'你好2'"
str3 = 'acd\'bef'  #最外面的单引号是一对 里面的单引号通过反斜杠\
print(str1)
print(str2)
print(str3)
print(str3[0])
print(str3[1])
print(str3[1:5]) #含头不含尾
print(str3[-2])
print(str3[2:]) #默认到最后
print(str3[:2])
print(str3[1:5:2]) #步长
print(str3[5:2:-1]) #步长





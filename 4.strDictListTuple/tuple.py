# -*-coding:utf-8-*-

'''

    创建元祖

    Python 的元组与列表类似，不同之处在于元组的元素不能修改。
    元组使用小括号，列表使用方括号。
    元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
'''

tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7)
'''
   -》访问元组 无论是不是多维的，都是通过下标去访问，同list
   -》元组索引，截取
        因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素，同list
'''
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])


'''
    
    修改元祖
    
    元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:
    
'''

tup1 = (12, 34.56);
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2;
print(tup3)


'''
    删除元组
    元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:
    
'''

tup = ('Google', 'Runoob', 1997, 2000)

print(tup)
del tup;#彻底删除
print("删除后的元组 tup : ")
#print(tup)


'''
    元组 内置函数
    len(tuple)计算元组元素个数。
    max(tuple)返回元组中元素最大值。
    min(tuple)返回元组中元素最小值。
    tuple(seq)将列表转换为元组。
'''

list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple1=tuple(list1)
print(tuple1)
print(type(tuple1))
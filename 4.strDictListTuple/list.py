# -*-coding:utf-8-*-
'''
    访问列v表
'''
list01 = ['jack', 'jane', 'joe','black']

print(list01[2])#通过下标访问

list02 = ['jack', 'jane', ['leonaldo','joe'],'black']

print(list02[2][0])
list02[0] = 'lili'  #通过下标获取元素，并且给其赋新值
print(list02)
list02[2][0] = 'susan'
print(list02)
#列表是一个可变的类型数据  允许我们对里面的元素进行修改




'''
    列表的添加操作
        -》append 往列表末尾增加元素
        -》insert 往列表中指定位置添加元素 list.insert(index, obj)
        index -- 对象obj需要插入的索引位置。
        obj -- 要插入列表中的对象。
'''
list02.append('老尹')
print(list02)

list1 = ['Google', 'Runoob', 'Taobao']
list1.insert(1, 'Baidu')
print ('列表插入元素后为 : ', list1)


'''
    删除列表元素
        -》 pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
            list.pop([index=-1])
            index -- 可选参数，要移除列表元素的索引值，不能超过列表总长度，默认为 index=-1，删除最后一个列表值
        -》del 语句通过指定位置来删除列表的的元素 指从内存中删除，根据索引
        -》remove list.remove(obj)用于移除列表中某个值的第一个匹配项。
            obj -- 列表中要移除的对象。
'''
list1 = ['Google', 'Runoob', 'Taobao']
list1.pop()
print ("列表现在为 : ", list1)
list1.pop(1)
print ("列表现在为 : ", list1)

list02 = ['Google', 'Runoob', 1997, 2000]
print("原始列表 : ", list02)
del list02[2]
print("删除第三个元素 : ", list02)

list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.remove('Taobao')
print ("列表现在为 : ", list1)
list1.remove('Baidu')
print ("列表现在为 : ", list1)


'''
    查找元素 in(存在) not in(不存在)
'''
list04 = ['jack','jane','joe','black']
name ='jack'
print('in 存在不',name in list04)

name ='jack'
print('not in 存在不',name not in list04)

'''
    列表函数
    -》len(list)方法返回列表元素个数  list -- 要计算元素个数的列表。
    -》max(list) 方法返回列表元素中的最大值。
    -》min() 方法返回列表元素中的最小值。
    -》list() 方法用于将元组或字符串转换为列表。
'''

list1 = ['Google', 'Runoob', 'Taobao']
print (len(list1))
list2=list(range(5)) # 创建一个 0-4 的列表
print (len(list2))

aTuple = (123, 'Google', 'Runoob', 'Taobao')
list1 = list(aTuple)
print ("列表元素 : ", list1)
str="Hello World"
list2=list(str)
print ("列表元素 : ", list2)

'''
    count() 方法用于统计某个元素在列表中出现的次数。
'''
aList = [123, 'Google', 'Runoob', 'Taobao', 123];
print ("123 元素个数 : ", aList.count(123))
print ("Runoob 元素个数 : ", aList.count('Runoob'))



'''
    extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
    list.extend(seq)
    seq -- 元素列表，可以是列表、元组、集合、字典，若为字典,则仅会将键(key)作为元素依次添加至原列表的末尾。
'''
list1 = ['Google', 'Runoob', 'Taobao']
list2=list(range(5)) # 创建 0-4 的列表
list1.extend(list2)  # 扩展列表
print ("扩展后的列表：", list1)


'''
    index() 函数用于从列表中找出某个值第一个匹配项的索引位置。
    list.index(x[, start[, end]])
    x-- 查找的对象。
    start-- 可选，查找的起始位置。
    end-- 可选，查找的结束位置。
'''
list1 = ['Google', 'Runoob', 'Taobao']
print ('Runoob 索引值为', list1.index('Runoob'))
print ('Taobao 索引值为', list1.index('Taobao'))

'''
    sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
    list.sort( key=None, reverse=False)
    ey -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
    reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
    该方法没有返回值，但是会对列表的对象进行排序。
'''
aList = ['Google', 'Runoob', 'Taobao', 'Facebook']

aList.sort()
print("List : ", aList)


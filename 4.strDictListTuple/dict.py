# -*-coding:utf-8-*-

'''

    字典

    -》字典是另一种可变容器模型，且可存储任意类型对象。
    -》字典是既能存储多个数据，又能方便准确的定位元素
    -》字典的每个键值(key=>value)对用冒号(:)分割，
    每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：

    d = {key1 : value1, key2 : value2 }
    键必须是唯一的，但值则不必。
    值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
    一个简单的字典实例：
    dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
    也可如此创建字典：
    dict1 = { 'abc': 456 }
    dict2 = { 'abc': 123, 98.6: 37 }
'''

dict01 = {'Name': 'joe', 'Age': 18, 'address': '上海'}
print(dict01)

'''
    访问字典
    
    字典中根据键访问值，可以指定自殿名和放在括号内的键，
'''
dict02 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print("dict02['Name']: ", dict02['Name'])
print("dict02['Age']: ", dict02['Age'])


'''
    修改字典元素
    
    通过找到指定的key进行修改

'''
dict02['Name']='jack'
print(dict02)

'''
    添加元素
    
    动态的向字典中添加元素的时候，只要添加的键在字典中不存在，就会新增这个元素，

'''
dict02['Address']='上海'

print(dict02)


'''
    删除字典
    
    del 字典名【key】  删除字典元素,直接删字典虽然可以删除，但是会报错
    clear 字典名.claer()  清空字典
'''
del dict02['Address'] #从内存中删除键‘Address’
dict02.clear()# 清空字典

'''
    字典内置函数&方法
    len(dict)计算字典元素个数，即键的总数。
    str(dict)输出字典，以可打印的字符串表示,即转换成字符串
    type(variable)返回输入的变量类型，如果变量是字典就返回字典类型。
'''
dict02 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(type(str(dict02)))

'''
    dict.get(key, default=None)返回指定键的值，如果值不在字典中返回默认值。
    key -- 字典中要查找的键。
    default -- 如果指定键的值不存在时，返回该默认值值
    #如果字典有该key对应的元素就输出原来的，如果没有就输出你指定的
'''
dict02 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First','sex':'女'}

print(dict02.get('sex','男'))

'''
    字典 in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false。
    而 not in 操作符刚好相反，如果键在字典 dict 里返回 false，否则返回 true。
    key in dict
'''

dict03 = {'Name': 'Runoob', 'Age': 7}

# 检测键 Age 是否存在
if 'Age' in dict03:
    print("键 Age 存在")
else:
    print("键 Age 不存在")

# 检测键 Sex 是否存在
if 'Sex' in dict03:
    print("键 Sex 存在")
else:
    print("键 Sex 不存在")

# not in

# 检测键 Age 是否存在
if 'Age' not in dict03:
    print("键 Age 不存在")
else:
    print("键 Age 存在")

'''
    dict.keys()方法返回一个可迭代对象，可以使用 list() 来转换为列表。
    dict.values()方法返回一个迭代器，可以使用 list() 来转换为列表，列表为字典中的所有值。
    注意：Python2.x 是直接返回列表
'''

dict02 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First','sex':'女'}
print(dict02.keys())
print(dict02.values())

'''
    dict.items()方法以列表返回可遍历的(键, 值) 元组数组。
'''
print(dict02.items())
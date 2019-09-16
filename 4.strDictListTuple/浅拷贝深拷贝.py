# -*-coding:utf-8-*-
import copy
'''
    直接赋值：其实就是对象引用 地址是同一个
'''
a = [1,2,3]
b = a
print(id(a)) #通过id查看变量在内存中的地址
print(id(b))

a[0] = 5
print(a)
print(b)#a和b是同一个地址

'''
    浅拷贝(copy)：拷贝父对象，不会拷贝对象的内部的子对象。
    b = a.copy(): 浅拷贝, a 和 b 是一个独立的对象，但他们的子对象还是指向统一对象（是引用）。
'''
a = [1,2,3]
b = [11,22,33]
c = [111,222,333]
list01 = [a,b,c]
print(id(list01))
list02 = list01[:]
print(list01)
print(list02)
#检查list01 和list02在内存中的地址
print(id(list01))
print(id(list02))

#修改一下
a[0]=5
print(list01)
print(list02)

'''
    深拷贝(deepcopy)： copy 模块的 deepcopy 方法，完全拷贝了父对象及其子对象。递归地拷贝全部
    b = copy.deepcopy(a): 深度拷贝, a 和 b 完全拷贝了父对象及其子对象，两者是完全独立的。
'''
a = [1,2,3]
b = [11,22,33]
c = [111,222,333]
list01 = [a,b,c]
print(id(list01))
list02 = copy.deepcopy(list01)
print('深',list01)
print(list02)

print(id(list01))
print(id(list02))

#修改一下
a[0]=5
print(list01)
print(list02)


# -*-coding:utf-8-*-




'''
'''
'''
  什么是函数？
    -》组织好的，可重复使用的，用户实现单一或者关联功能的代码段
  函数的作用？
    -》提高应用的模块性，和代码的重复使用率 
'''
'''
    函数的定义：
    def 函数名([参数]):
        #函数说明
        要封装的代码块
'''


def Pname():    #当前函数不放参数
    '''
    获取姓名
    :return:
    '''
    print('大家好，我是小明同学')

#有参数吗？ 很明显没有

Pname() #调用函数


pri =Pname #将函数名赋值给另一个变量  ，给当前函数去一个别名
pri()




# def getNum():   #定义函数用驼峰
#     print('100')
# getNum()#调用函数





'''
    函数的参数
'''
def getName(userName):    #当前函数userName 形参 形参名字是自定义的
    '''
    获取姓名
    :return:
    '''
    print('大家好，我是%s同学'%userName)

getName('刘德华')  #传递了一个实参



'''
    必备参数
    #参数的个数不能少，不能多。 参数的位置要一一对应
'''
def getInfo(name, address):
    print('大家好我叫%s,我来自%s'%(name,address))

getInfo('刘德华','香港')

#参数的个数不能少，不能多。 参数的位置要一一对应


'''
    关键字参数
'''
def getInfo(name, address):
    print('大家好我叫%s,我来自%s'%(name,address))

getInfo(address='香港',name='刘德华')#给实参加上关键字。关键字对应我们的形参


'''
    参数默认值
    就是在声明函数的时候给默认值
'''
def getInfo(name, address='香港'):#带默认值的参数放在右面
    print('大家好我叫%s,我来自%s'%(name,address))

getInfo('刘德华','九龙') #传递参数的话，会覆盖原来的默认值


'''
    不定长参数
'''
def getInfo(name, address,*args,**args2):#带默认值的参数放在右面
    print('大家好我叫%s,我来自%s'%(name,address))
    print(args) #args 是一个元组类型 接收所有未命名的参数(关键字)
    print(args2) #字典数据类型（带关键字）


getInfo('刘德华','九龙','a','b','c',age=18)


'''
    标记函数
    
    值传递 ： 不可变对象的传递
'''
def sign():
    print('_'*50)
def fun(args):
    args = 'hello'
    print(args)

str1 = 'baby' #声明一个字符串的变量 不可变数据类型
fun(str1) #将该字符串传递到函数中
sign()
print(str1)#还是baby 并没有被改变


'''
    引用传递 ：可变对象的传递
'''
def fun(args):
    args[0] = 'he' #重新赋值
    print(args)

list01=['baby','come on']
fun(list01)
sign()
print(list01) #传递的是对象本身，函数里面被修改了值，原对象也会跟着修改

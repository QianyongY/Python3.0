#-*- conding:utf-8 -*-
class person():
    '''
        这是一个人类
    '''
    country = '中国'  #声明类属性，并且赋值
    #实例属性通过构造方法来声明
    #self不是关键字，代表的是当前而对象
    def __init__(self,name,age,sex,address): #构造方法
        #构造方法不需要调用，在实例化的时候自动调用
        # print('我是构造方法，在实例化得时候调用')
        self.name = name  #通过self 创建实例属性，并且赋值
        self.age = age
        self.sex = sex
        self.__address = address #双下划线开头的属性是私有属性


    #创建普通方法
    def getName(self):
        #类属性的使用通过类名.属性名使用 这是规范
        #私有属性在类里面使用正常使用
        print('我的名字叫：%s,我来自%s,我住在%s'%(self.name,person.country,self.__address)) #在方法里面使用实例属性

    #外部要修改私有属性  预留一个借口去访问或者修改私有属性  这个就是正确的打开方式
    def getAddre(self,pwd):
        if pwd == '123':
            return self.__address
        else:
            return '权限不够'



#实例化对象
people01 = person('joe',19,'男','上海')
people01.getName()
#通过对象名.属性名访问私有属性
# print(people01.__address)   #外部无法使用 这种方式访问

print(people01.getAddre('1234'))

#强制访问
print(people01._person__address)

people01.__address = '北京'  #看上去好像改了，其实没有  你给当前对象声明了一个新属性
print(people01.__address)


print(people01.getAddre('123'))
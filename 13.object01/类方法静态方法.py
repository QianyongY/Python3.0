#-*- conding:utf-8 -*-
#-*- conding:utf-8 -*-
class person():
    '''
        这是一个人类
    '''
    country = '中国'  #声明类属性，并且赋值
    #实例属性通过构造方法来声明
    #self不是关键字，代表的是当前而对象
    def __init__(self,name,age,sex,address):#country) #构造方法
        #构造方法不需要调用，在实例化的时候自动调用
        # print('我是构造方法，在实例化得时候调用')
        self.name = name  #通过self 创建实例属性，并且赋值
        self.age = age
        self.sex = sex
        self.__address = address #双下划线开头的属性是私有属性
        #person.country = country
    #创建普通方法
    def getName(self):
        #类属性的使用通过类名.属性名使用 这是规范
        #私有属性在类里面使用正常使用
        print('我的名字叫：%s,我来自%s,我住在%s'%(self.name,person.country,self.__address)) #在方法里面使用实例属性

    #创建一个静态方法
    @staticmethod
    def aa():  #不需要传递实例
        #静态方法不能访问实例属性
        #静态方法只能访问类属性
        print('我的名字叫：%s' % person.country)  # 在方法里面使用实例属性


    #类方法
    @classmethod
    def bb(cls,n):  #class  也不是关键字
        #类方法也不能访问实例属性
        cls.country = n
        print('我的名字叫：%s' %cls.country )  #就用cls.类属性


#实例化对象
people01 = person('joe',19,'男','上海')

# #通过对象来调用静态方
# people01.aa()
# #通过对象来调用类方法
# people01.bb()




#静态方法和类方法的调用，推荐使用类名的方式去调用
#通过类名来调用静态方法
person.aa()
#通过类名来调用类方法
person.bb('usa')
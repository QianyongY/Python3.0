#-*- conding:utf-8 -*-

class A():
    def a(self):
        print('我是A里面的a方法')

class B():
    def b(self):
        print('我是B里面的b方法')

    def a(self):
        print('我是B里面的a方法')

class C():
    def c(self):
        print('我是C里面的c方法')

class D(A,B,C):
    def d(self):
        print('我是D里面的d方法')

dd = D()
dd.d() #调用自己的方法
dd.c()

dd.a()

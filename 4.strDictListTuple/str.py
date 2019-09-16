# -*-coding:utf-8-*-
'''
    格式化输出方式
'''
name = 'joe'
age = 18
address = '上海'
# print('大家好，我叫%s ,我今年%d岁，我来自%s'%(name,age,address))#   f 浮点数


'''
    字符串常用函数
'''


#  1.  find str.find(str, beg=0, end=len(string)) 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1
'''
str -- 指定检索的字符串
beg -- 开始索引，默认为0。
end -- 结束索引，默认为字符串的长度。
'''

str = 'i love python'

'''
print('返回的是该字符首次出现的位置',str.find('o')) #返回的是该字符首次出现的位置下标索引值
print('返回的是从下标4开始，该字符首次出现的位置',str.find('o',4)) # 从下标4开始，查找在字符串里第一个出现的子串：返回结果下标
print('返回的是该字符首次出现的位置',str.find('i'))
print('查找不到返回',str.find('w'))  #返回 -1 可用于注册字符串检验
'''

#  2.   index 跟find()方法一样，只不过如果str不在字符串中会报一个异常.
'''
print('index返回的是该字符首次出现的位置',str.index('o')) #返回的是该字符首次出现的位置下标
print('index返回的是从下标4开始，该字符首次出现的位置',str.index('o',4)) # 从下标4开始，查找在字符串里第一个出现的子串：返回结果下标
print('index返回的是该字符首次出现的位置',str.index('i'))
print('index查找不到返回',str.index('w'))  #返回 异常
'''


#   3.   count   str.count(sub, start= 0,end=len(string)) 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
'''
sub -- 搜索的子字符串
start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。
'''

#print('count返回的是该字符出现的次数',str.count('o'))
# print('count返回的是该字符出现的次数',str.count('o',2,6))
# print('count查找不到返回',str.count('w'))  #返回 异常

#   4.   replace str.replace(old, new[, max]) 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
'''
old -- 将被替换的子字符串。
new -- 新字符串，用于替换old子字符串。
max -- 可选字符串, 替换不超过 max 次
'''

# print('repalce替换结果：',str.replace('o','O'))
# print('repalce替换1次结果：',str.replace('o','O',1))



#   5.  split str.split(str="", num=string.count(str)) 通过指定分隔符对字符串进行切片，如果第二个参数 num 有指定值，则分割为 num+1 个子字符串。
'''
str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
num -- 分割次数。默认为 -1, 即分隔所有。
'''
# print('split以空格为分隔符结果：',str.split(' ')) #返回结果列表
# print('split 1次结果：',str.split('o',1))
# print('split 结果：',str.split('o'))


#    6.upper()转换字符串中的小写字母为大写
'''
     title()返回"标题化"的字符串,就是说所有单词都是首字母大写，其余字母均为小写(见 istitle())
     capitalize()将字符串的第一个字符转换为大写

'''

# str = "this is string example from runoob....wow!!!"
# print ("str.capitalize() : ", str.capitalize())

#    7.center(width, fillchar) 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
'''
    width -- 字符串的总宽度。
    fillchar -- 填充字符。
'''

str = "[www.runoob.com]"

print ("str.center(40, '*') : ", str.center(40, '*'))
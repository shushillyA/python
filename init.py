# print('请输入两个整数')
# name1 = input()
# name2 = input()
# c = int(name1) + int(name2) + 1
# print(c)



# print(r"\\t\\\\\\\\\\\\")

# print('''
# ahhh
# ahhh
# fdaf
# fdas
# ''')

# 换行并且空一行
# print(r"\n显示",'''hello,\n
# world''')
# print('\r')
# 换行
# print(r"\r显示",'''hello,\r
# world''')
# 单独使用\r会报错
# print(r"\r显示",'\r','''hello,\r
# world''')


# / 浮点数

# // 永远是整数

# % 取余

# python使用unicode
# 以下方法转成utf-8 1到6个字节组成
# 获取字符
# str = chr(31231)
# print('显示的字符', str)
# 获取编码
# aUcode = ord(str)
# print('字符代码', aUcode)

# python类型 str bytes 







# 数组list
# a = [1,2,3]
# print(len(a)) #长度
# 方法 pop append push insert插入 


# tuple不可变
# t = (1,2,3)
# print(t)

# aa1 = 2
# bb1 = 2
# if aa1>bb1:
#   print('大')
# elif aa1 == bb1:
#   print('等')
# else: 
#   print('小')

# 等差数列
# l = list(range(10))
# print(len(l))

# L = ['Bart', 'Lisa', 'Adam']
# for x in L:
#   print('hello', x)

# 对象dict
# obj = {'a':1,'b':2,'c':3}
# result = 'a' in obj  # False
# print(result)
# r2 = obj.get('b', -1) # 复制不顶替原来的
# print(r2) # None

# 对象移除
# obj.pop('c') # 移除C
# print(obj)

# set === 没有值的dict 无序
# s1 = set([1,2,3,3,2,1]) # 重复的删除
# s2 = set([1,2,3,4,5,6,7,8,9,0,4,'baba'])
# s1.add(5) #添加一个数
# s1.remove(5) #移除
# print(s1)
# s3 = s1 | s2 // 幷集
# s4 = s1 & s2 // 交集
# print(s3,s4)

# python 字符串也是个对象
# a = 'aBc'
# b = a.replace('B', 'b')
# print(a,b)

# 函数调用
# abs(100)
# max(1,2,3)
# int()
# float()
# str()
# bool()

# 定义函数
def func(x=2):
  if not isinstance(x, (int,float)):
    raise TypeError('你输的啥啊') #提示报错 相当于try catch
  pass #占位符 差不多等于return
  return 321, 313
a = func() # 这边和js不一样 如果不传 就会报错 设置默认就不会报错了
print(a) #a是个tuple => 不可改变的数组

# 返回值
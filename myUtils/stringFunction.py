#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########字符串的一些常用的方法：###################################

# 字符串在中间，总共是20位，不够的用*号填充
# s = "apple"
# s = s.center(20, "*")
# print(s) # *******apple********


# 统计字符串里面有几个p字母
# s = "apple apple apple apple"
# s = s.count("p")
# print(s) # 8

# 从5索引开始到最后这中间有多少个p字母
# s = "apple apple apple apple"
# s = s.count("p", 5)
# print(s) # 包括5索引处的p


# 从5索引开始到8索引这中间有多少个p字母
# s = "apple apple apple apple"
# s = s.count("p", 5, 8)
# print(s)

# 判断字符串是否以le结尾，是返回真，否就返回假
# s = "apple"
# print(s.endswith("le"))

# 判断字符串是否以ap开头，返回布尔值
# s = "apple"
# print(s.startswith("ap"))

# 从索引2开始检查，是否已p开头，6索引结束，不写6，就认为从2索引到最后
# s = "apple apple apple"
# print(s.startswith("p", 2, 6))

# 查找字符串中pl在哪个位置，返回索引值。s.find("pl, 3, 8")，表示3索引开始，8索引结束，找不到返回-1
# s = "apple apple dog cat"
# print(s.find("pl"))

# {name} 占位，format传入一个key=value形式的参数，value就会替换{name},大括号里的内容和key保持一致
# s = "hello {name}"
# s = s.format(name="jack")
# print(s)

# format_map传入的就是一个字典
# s = "hello {name} {age}"
# s = s.format_map({"name": "jack", "age": 18})
# print(s)

# 判断是否只包含数字和字母，返回真假值
# s = "apple"
# print(s.isalnum())

# 第一行从u(username)前面到e(email)前面是20个空格，从e(email)前面到p(password)前面是20个空格。
# 即：username\t的空格数=email\t的空格数=20个空格
# s = "username\temail\tpassword\njack\tying@q.com\t123\njack\tying@q.com\t123\njack\tying@q.com\t123"
# print(s.expandtabs(20))

# 判断字符串是否只包含字母，返回真假
# s = "apple"
# print(s.isalpha())

# 判断当前字符串是否都是数字
# s = "12345"
# print(s.isdecimal())

# s = "12345②"
# print(s.isdigit())

# s = "123456"
# print(s.isnumeric())

# 判断符不符合标识符规则
# s = "abc0"
# print(s.isidentifier())

# 将字符串里面所有字母变小写
# s = "APPLE"
# print(s.lower())

# 判断字符串里面的每个字母是否是小写，返回布尔值
# s = "apple1"
# print(s.islower())

# 将字符串所有的字母都变大写
# s = "apple"
# print(s.upper())

# 判断字符串里的所所有字母是否都是大写，返回布尔值
# s = "apple"
# print(s.isupper())

# 判断是否有不可见的字符???
# s = "apple"
# print(s.isprintable())

# 判断是否全部都是空格，返回布尔值
# s = "  \t   "
# print(s.isspace())

# 判断每个单词的首字母是否大写，返回布尔值
# s = "Apple Apple Apple"
# print(s.istitle())

# 将每个单词的首字母大写其他的字母变小写
# s = "apple apple APPLE"
# print(s.title())

# 将字符串的每个字符用引号里的字符连接起来
# s = "apple"
# print("*".join(s))

# 占20个位置，除字符串占用的外，剩下的用引号里的字符填充
# s = "apple"
# print(s.ljust(20, "*")) 左填充
# print(s.rjust(20, "*")) 右填充

# 左边填充0
# s = "apple"
# print(s.zfill(10))

# 左边去空格，右边去空格，两端去空格
# s = "  app  le  "
# print(s.lstrip())
# print(s.rstrip())
# print(s.strip())

# 将字符串里的a全部替换为*，2是要替换的个数，没有就全部替换，比如字符串里面有三个a，第三个参数为2，只是将前两个a替换了
# s = "apple apple apple dog"
# print(s.replace("a", "*", 2))

# a-1,s-2,p-3 对应替换字符串中的字符
# s = 'apple dog jack english'
# m = str.maketrans('asp', '123')
# new_s = s.translate(m)
# print(new_s)

# 找到第一个e就分割，变成三份
# s = "applePyAppleCharmAppleEnglish"
# print(s.partition("e")) 从左往右找

# s = "applePyAppleCharmAppleEnglish"
# print(s.rpartition("e")) 从右往左找

# 遇见p就分割，切p字符消失，若是连着的4个p，则后3个p变'' |*****
# s = "aple apleapppple"
# print(s.split("p"))
# print(s.split("p", 2))  # 只遇见第一个p分割，后面的不分割
# print(s.rsplit("p"))

# 以换行符分割
# s = "qdafg\nhdhfj\ndfdddfgsdf"
# print(s.splitlines())
# print(s.splitlines(True))

# 是否以..开头 ..结尾 返回布尔值
# s = "apple"
# print(s.startswith("a"))
# print(s.endswith("e"))

# 将字符串中的大写字母转小写，小写转大写
# s = "aPPle"
# print(s.swapcase())

# 将第一个字母变大写，其他的都小写
# s = "apPle Apple"
# print(s.capitalize())

# #######切片操作###########
# 切片之后除非赋值给原变量，不然原字符串没改变
# a = "apple apple dog jack alex"
# b = a[0:8]  # 截取0索引到8索引之间的字符串，不包括8索引
# b = a[:]    # 相当于复制了一份
# b = a[2:]   # 2索引开始，直到结束
# b = a[:8]   # 从开始索引到8索引之间
# print(b)

# #######list列表操作：###########

# a = [321, 'xyz', 'zara', 'abc', 123]
# b = [2009, 'man']
# c = [12.23, 15, 7, 3, 77]
# f.append("apple")      # 添加到末尾
# f.clear()              #清空所有元素
# a = f.copy()   	     #复制列表
# a = f.count("apple")   # 统计列表里面有几个这样的元素
# aList.extend(bList)    # 将b列表的元素全部添加到a列表里面
# k = a.index("abc")       # 返回abc元素的位置，没有abc元素就报错
# a.insert(0, 789)      # 在0索引处增加一个元素
# kk = a.pop()  # 没参数默认移除最后一个元素，可以添加索引弹出指定的元素，弹出的元素可以被接收
# a.remove()  # 必须传入要移除的元素，移除后就没有了 print(a.remove(123))为None
# del a[0]  # 删除一个元素
# del a[0:3] #删除0 1 2 三个位置的元素
# a.reverse() # 反转列表，改变的是原来的列表
# c.sort() # 按字母从小到大排序，永久改变了原来列表
# c.sort(reverse=True) # 从大到小排序
# sorted()  对列表进行临时排序,不影响原始列表，也可以传递参数reverse=True
# kk = enumerate(a) # enumerate()方法里面传入一个列表，得到的是个地址值，list（地址值），得到一个数据和数据下标对应的列表
# print(list(kk))


# #########字典##########
dic1 = {"apple": "001", "dog": "002", "cat": "dog", "jack": "ros"}
dic2 = {"郭靖": "黄蓉", "张无忌": "赵敏", "杨过": "小龙女", "apple": "苹果"}
# for k in dic:
# 	print(k) # 直接遍历字典遍历的是key

# print(dic.keys())  # 返回迭代器 dict_keys(['apple', 'dog', 'cat', 'jack'])
# print(list(dic.keys()))  # 用list直接转换成列表 ['apple', 'dog', 'cat', 'jack']
# print(dic.values())  # 同上
# print(dic.items())  # dict_items([('apple', '001'), ('dog', '002'), ('cat', 'dog'), ('jack', 'ros')])
# print(list(dic.items()))  # [('apple', '001'), ('dog', '002'), ('cat', 'dog'), ('jack', 'ros')]

# seq = ('z', 'x', 'y')
# di = dict.fromkeys(seq, 10)  # fromkeys() 函数用来构建一个新字典
# print(di)  # 没有10时键默认None{'z': None, 'x': None, 'y': None}
# print(di)  # {'z': 10, 'x': 10, 'y': 10}

# print(dic.pop("apple", "NoKey"))  # 删除apple：001 这对元素，返回key对应的值，不存在键，就返回默认值noKey

# print(dic.popitem())  # 返回并删除字典中的最后一位键值对

# dic.setdefault("apple", '100')  # 键存在，原样输出
# dic.setdefault("banana", "香蕉")  # 键不存在，天加进去
# dic1.update(dic2)  # d1中没有键的就添加进来，d1中有的键，其值就用d2中的值替换

# kk = dic1.get("apple", "默认")  # 返回指定键对应的值，没有就返回默认


# #########集合（无序，不重复）##########
x = {"apple", "banana", "cherry"}
y = {"google", "run", "apple"}

# a = set()  # 创建空集合
# s1 = set(("Google", "Run", "TaoBao"))
# s2 = set(["Google", "Run", "TaoBao"])
# s3 = set({"湖北": "武汉", "湖南": "长沙", "广东": "广州"})  # {'湖南', '广东', '湖北'}


# x.add("dog") # 添加一个元素
# x.update({"cat"})  # 也可以添加一个元素
# x.update(["jack", "alex"])  # 也可以添加...个元素
# x.discard("apple")  # 移除 元素不存在不会发生错误 没有返回值
# x.remove("apple")  # 移除 元素不存在会发生错误 没有返回值
# a = x.pop()  # 随机删除一个元素

# intersection()==& 交集
# union()==| 并集
# difference() == - 差集
# difference_update() 求出查缉之后赋值给原来的变量
# symmetric_difference() == ^  交叉补集
# isdisjoint() 无交集返回真
# issubset()A是B的子集 返回真
# issuperset()A是B的父集 返回真
# update() 更新多个值
# s=frozenset('hello')  定义不可变集合

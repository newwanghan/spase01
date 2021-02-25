import pandas as pd

# 我们的小数据集
d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 创建一个 dataframe
df = pd.DataFrame(d)
# 我们把列名修改一下
df.columns = ['Rev']
# 我们增加一列
df['NewCol'] = 5
# 修改一下新增加的这一列的值
df['NewCol'] = df['NewCol'] + 1
# 我们可以删除列
del df['NewCol']
# 让我们增加几列。 译者注: 当使用 dataframe 没有的列时，dataframe 自动增加这个新列
df['test'] = 3
df['col'] = df['Rev']
# 如果有需要，可以改变索引(index)的名字
i = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df.index = i
# print(df)
# print(df.loc['a'])
# df.loc[起始索引(包含):终止索引(包含)]
# print(df.loc['a':'d'])
# 可以通过列名选择一列的值。
# print(df['Rev'])
# 选择几列
# print(df[['Rev', 'test']])

# 我们的小数聚集
d = {'one': [1, 1], 'two': [2, 2]}
i = ['a', 'b']
# 创建一个 dataframe
df = pd.DataFrame(data=d, index=i)
print(df)
print(df.index)
stack = df.stack()
print(stack)
print(stack.index)
unstack = df.unstack()
print(unstack)
print(unstack.index)
# 用 T (转置)，我们可以把列和索引交换位置。
transpose = df.T
print(transpose)
print(transpose.index)

# 我们的小数聚集
d = {'one': [1, 1, 1, 1, 1],
     'two': [2, 2, 2, 2, 2],
     'letter': ['a', 'a', 'b', 'b', 'c']}
# 创建一个 dataframe
df = pd.DataFrame(d)
print(df)
# 创建一个 groupby 对象
one = df.groupby('letter')
# 在分组上应用 sum() 函数
print(one.sum())
letterone = df.groupby(['letter', 'one']).sum()
print(letterone)
print(letterone.index)
# 不想把用来分组的列名字作为索引，像下面的做法很容易实现。
letterone = df.groupby(['letter','one'], as_index=False).sum()
print(letterone)
print(letterone.index)

import pandas as pd
import numpy.random as np
# import numpy as np
import matplotlib.pyplot as plt

# from numpy import random

names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
# births = [968, 155, 77, 578, 973]
# BabyDataSet = list(zip(names, births))
# print(BabyDataSet)
# df = pd.DataFrame(data=BabyDataSet, columns=['Names', 'Births'])
# print(df)
# df.to_csv('births1880.csv', index=False, header=False)

# Location = r'./births1880.csv'
# df = pd.read_csv(Location)
# df = pd.read_csv(Location, header=None)
# df = pd.read_csv(Location, names=['Names', 'Births'])
# print(df)
# 查看每一列的数据类型
# print(df.dtypes)
# 查看 Births 列的数据类型
# print(df.Births.dtype)

# 找出Births列中的最大值
# 方法 1:
# Sorted = df.sort_values(['Births'], ascending=False)
# print(Sorted.head(1))
# # 方法 2:
# print(df['Births'].max())
# print(df['Names'])
# var = [df['Births'] == df['Births'].max()] # [在Births列中找到值是973 的所有记录]
# print(var)
# var = df['Names'][df['Births'] == df['Births'].max()]  # 在 Names列中挑选出 [Births 列的值等于 973]
# print(var)
# print(Sorted['Names'].head(1).values)
#
# # 绘图
# # df['Births'].plot()
# df['Births'].plot.bar()  # 这里改用的条形图更直观
# # Births 中的最大值
# MaxValue = df['Births'].max()
# print('MaxValue:', MaxValue)
# # 找到对应的 Names 值
# MaxName = df['Names'][df['Births'] == df['Births'].max()].values
# print("MaxName:", MaxName)
# # 准备要显示的文本
# Text = str(MaxValue) + " - " + MaxName
# # 将文本显示在图形中
# plt.annotate(Text, xy=(1, MaxValue), xytext=(8, 0), xycoords=('axes fraction', 'data'), textcoords='offset points')
# plt.show()
# print("The most popular name")
# a = df[df['Births'] == df['Births'].max()]
# print(a)


# random.seed(500)
# random_names = [names[random.randint(low=0, high=len(names))] for i in range(1000)]
# print(random_names)
# births = [random.randint(low=0, high=1000) for i in range(1000)]
# print(births)
# BabyDataSet = list(zip(random_names, births))
# print(BabyDataSet)
# df = pd.DataFrame(data=BabyDataSet, columns=['Names', 'Births'])
# df.to_csv('births1880_1000.csv', index=False, header=False)

# Location = r'./births1880_1000.csv'
# df = pd.read_csv(Location, names=['Names', 'Births'])
# print(df.info())
# print(df['Names'].unique())  # 找出 "Names" 列的所有唯一的(unique)的记录。
# print(df['Names'].describe())
# 创建一个 groupby 的对象
# name = df.groupby('Names')
# print(name)
# # 在 groupby 对象上执行求和(sum)的功能
# df = name.sum()
# print(df)

# 设置种子
np.seed(111)


# 生成测试数据的函数
def CreateDataSet(Number=1):
    Output = []
    for i in range(Number):
        # 创建一个按周计算的日期范围(每周一起始)
        rng = pd.date_range(start='1/1/2009', end='12/31/2012', freq='W-MON')
        # 创建一些随机数
        data = np.randint(low=25, high=1000, size=len(rng))
        # 状态池
        status = [1, 2, 3]
        # 创建一个随机的状态列表
        random_status = [status[np.randint(low=0, high=len(status))] for k in range(len(rng))]
        # 行政州(state)的列表
        states = ['GA', 'FL', 'fl', 'NY', 'NJ', 'TX']
        # 创建一个行政周的随机列表
        random_states = [states[np.randint(low=0, high=len(states))] for j in range(len(rng))]
        Output.extend(zip(random_states, random_status, data, rng))
    return Output


# dataset = CreateDataSet(4)
# df = pd.DataFrame(data=dataset, columns=['State', 'Status', 'CustomerCount', 'StatusDate'])
# print(df.info())
# df.to_excel('Lesson3.xlsx', index=False)  # 不保存索引，但是保存列名(column header)
# print('Done')
Location = r'./Lesson3.xlsx'
df = pd.read_excel(Location, sheet_name=0, index_col='StatusDate')
# print(df)
# print(df.dtypes)
# print(df.index)
# print(df.head())
# 清洗 State 列，全部转换为大写
df['State'] = df.State.apply(lambda x: x.upper())
print(df['State'].unique())
# 只保留 Status == 1
mask = df['Status'] == 1
df = df[mask]
print(df)
# 将 NJ 转换为 NY
# [df.State == 'NJ'] - 找出 State 列是 NJ 的所有记录。
# df.State[df.State == 'NJ'] = 'NY' - 对 State 列是 NJ 的所有记录，将其替换为NY
mask = df.State == 'NJ'
df['State'][mask] = 'NY'
print(df['State'].unique())
# df['CustomerCount'].plot(figsize=(15, 5))
# plt.show()
sortdf = df[df['State'] == 'NY'].sort_index(axis=0)
print(sortdf.head(10))
# 先 reset_index，然后按照 State 和 StatusDate 来做分组 (groupby)
Daily = df.reset_index().groupby(['State', 'StatusDate']).sum()
print(Daily.head())
del Daily['Status']
print(Daily.head())
print(Daily.index)
# 选择 State 这个索引
print(Daily.index.levels[0])
print(Daily.index.levels[1])
# Daily.loc['FL'].plot()
# Daily.loc['GA'].plot()
# Daily.loc['NY'].plot()
# Daily.loc['TX'].plot()
# plt.show()
# 计算离群值
StateYearMonth = Daily.groupby(
    [Daily.index.get_level_values(0), Daily.index.get_level_values(1).year, Daily.index.get_level_values(1).month])
Daily['Lower'] = StateYearMonth['CustomerCount'].transform(
    lambda x: x.quantile(q=.25) - (1.5 * x.quantile(q=.75) - x.quantile(q=.25)))
Daily['Upper'] = StateYearMonth['CustomerCount'].transform(
    lambda x: x.quantile(q=.75) + (1.5 * x.quantile(q=.75) - x.quantile(q=.25)))
Daily['Outlier'] = (Daily['CustomerCount'] < Daily['Lower']) | (Daily['CustomerCount'] > Daily['Upper'])
# 移除离群值
Daily = Daily[Daily['Outlier'] == False]
print(Daily.head())
# 按日期计算出最大的客户数
ALL = pd.DataFrame(Daily['CustomerCount'].groupby(Daily.index.get_level_values(1)).sum())
ALL.columns = ['CustomerCount']  # rename column
# 按照年和月来分组
YearMonth = ALL.groupby([lambda x: x.year, lambda x: x.month])
# 找出每一个年和月的组合中最大的客户数
ALL['Max'] = YearMonth['CustomerCount'].transform(lambda x: x.max())
print(ALL.head())
data = [1000, 2000, 3000]
idx = pd.date_range(start='12/31/2011', end='12/31/2013', freq='A')
BHAG = pd.DataFrame(data, index=idx, columns=['BHAG'])
print(BHAG)
# 把 BHAG 和 ALL 两个数据集合并在一起
combined = pd.concat([ALL, BHAG], axis=0)
combined = combined.sort_index(axis=0)
print(combined.tail())
fig, axes = plt.subplots(figsize=(12, 7))
combined['BHAG'].fillna(method='pad').plot(color='green', label='BHAG')
combined['Max'].plot(color='blue', label='All Markets')
plt.legend(loc='best')
# plt.show()
# Group by Year and then get the max value per year
Year = combined.groupby(lambda x: x.year).max()
Year['YR_PCT_Change'] = Year['Max'].pct_change(periods=1)
print(Year)
print((1 + Year.loc[2012:, 'YR_PCT_Change']) * Year.loc[2012:, 'Max'])
# 第一张图是整个市场的
ALL['Max'].plot(figsize=(10, 5));
plt.title('ALL Markets')
# 后面四张
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 10))
fig.subplots_adjust(hspace=1.0)  # Create space between plots
Daily.loc['FL']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[0, 0])
Daily.loc['GA']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[0, 1])
Daily.loc['TX']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[1, 0])
Daily.loc['NY']['CustomerCount']['2012':].fillna(method='pad').plot(ax=axes[1, 1])
# 增加图表的抬头
axes[0, 0].set_title('Florida')
axes[0, 1].set_title('Georgia')
axes[1, 0].set_title('Texas')
axes[1, 1].set_title('North East')
plt.show()

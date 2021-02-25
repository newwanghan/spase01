import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)
# d = pd.date_range('20200101', periods=6)
# print(d)
# df = pd.DataFrame(np.random.randn(6, 4), index=d, columns=list('ABCD'))
# print(df)
# print('----------------------df----------------------')
# d02 = pd.DataFrame({'A': 1,
#                     'B': pd.Timestamp('20200101'),
#                     'C': pd.Series(1, index=list(range(6)), dtype='float32'),
#                     'D': np.array([3] * 6, dtype='int32'),
#                     'E': np.array(['haha1', 111, 'haha2', 222, 'haha3', 333]),
#                     'F': pd.Categorical(['test1', 'test2', 'test3', 'test4', 'test5', 'test6']),
#                     'G': 'foo'})
# print(d2)
# print(d2.dtypes)
# print(d2.head())
# print(d2.head(3))
# print(d2.tail())
# print(d2.tail(3))
# print(df.index)
# print(d2.index)
# print(df.columns)
# print(df.values)
# print(d2.values)
# print(df.describe())
# count：返回数组的个数(几行)，如上述为4个元素，所以返回为4；
# mean：返回数组的平均值，1 3 5 9的平均值为4.5；
# std：返回数组的标准差；
# min：返回数组的最小值；
# 25%，50%，75%：返回数组的三个不同百分位置的数值，也就是统计学中的四分位数，其中50%对应的是中位数。
# max：返回列表的最大值。
# print(df.T)
# print(df.sort_index(axis=0, ascending=False))
# axis：0按照行名排序；1按照列名排序, ascending：默认True升序排列；False降序排列
# print(df.sort_values(by='2020-01-03', axis='columns'))
# axis：{0 or ‘index’, 1 or ‘columns’}, default 0，默认按照列排序，即纵向排序；如果为1，则是横向排序。
# 行
# print(df.loc[d[[1, 4]]])
# print(df.loc['2020-01-04'])
# print(df.loc[d[3]])
# print(df.loc['20200102': '20200105'])
# print(df.loc[['20200102', '20200105']])
# 列
# print(df['C'])
# print(df.loc[:, 'C'])
# print(df.loc[:, 'A':'C'])
# print(df.loc[:, ['B', 'D']])
# 块
# print(df.loc['20200103': '20200104', 'B':'C'])
# print(df.loc[['20200102', '20200104'], ['A', 'C']])
# print(df.loc['20200102':'20200104', ['A', 'C']])
# print(df.loc[['20200102', '20200104'], 'A': 'C'])
# 单元格
# print(df.loc['20200104', 'D'])
# print(df.at['20200104', 'D'])

# print(df.iloc[0])
# print(df.iloc[1: 3])
# print(df.iloc[[1, 3]])


# print(df.iloc[:, 2])
# print(df.iloc[:, 0:3])
# print(df.iloc[:, [1, 3]])

# print(df.iloc[1: 3, 1:3])
# print(df.iloc[[0, 2], [0, 2]])
# print(df.iloc[0:3, [0, 2]])
# print(df.iloc[[0, 3], 0: 2])
# print(df.iloc[4, 1])

# print(df[df.A > 0])
# print(df[df > 0])
# d2 = df.copy()
# d2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
# print(d2)
# print(d2[d2['E'].isin(['two', 'four'])])

# s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20200102', periods=6))
# print(s1)
# df['F'] = s1
# print(df)
# df.at[d[0], 'A'] = 0
# df.iat[0, 1] = 0
# df.loc[:, 'D'] = np.array([5] * len(df))
# print(df)

# df2 = df.copy()
# df2[df2 > 0] = -df2
# # print(df2)
# df1 = df.reindex(index=d[0:4], columns=list(df.columns) + ['E'])
# df1.loc[d[0]: d[1], 'E'] = 1
# print(df1)
# print(df1.dropna(how='any'))
# print(df1.fillna(value=66))
# print(pd.isnull(df1))
# print(df.mean(1))  # 每一行的平均值
# print(df.mean())  # 每一列的平均值
# s = pd.Series([1, 3, 5, np.nan, 6, 8], index=d).shift(2)  # 列元素偏移两位
# print(s)
# print(df.sub(s, axis='index'))  # 对不同维度的 pandas 对象进行减法操作

# print(df.apply(np.cumsum))  # 每一列向下累加
# print(df.apply(lambda x: x.max() - x.min()))

# s = pd.Series(np.random.randint(0, 7, size=10))
# print(s)
# print(s.value_counts())  # 统计没个值出现了几次

# s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
# print(s.str.lower())

# df = pd.DataFrame(np.random.randn(10, 4))
# print(df)
# pieces = [df[:3], df[7:]]
# print(pd.concat(pieces))

# left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
# print(left)
# right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
# print(right)
# print(pd.merge(left, right, on='key'))

# s = df.iloc[3]
# print(s)
# print(df.append(s, ignore_index=False))

# df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
#                          'foo', 'bar', 'foo', 'foo'],
#                    'B': ['one', 'one', 'two', 'three',
#                          'two', 'two', 'one', 'three'],
#                    'C': np.random.randn(8),
#                    'D': np.random.randn(8)})
# print(df)
# print(df.groupby('A').sum())
# print(df.groupby(['A','B']).sum())

# tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
#                      'foo', 'foo', 'qux', 'qux'],
#                     ['one', 'two', 'one', 'two',
#                      'one', 'two', 'one', 'two']]))
# print(tuples)
# index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
# print(index)
# df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
# print(df)
# df2 = df[:4]
# print(df2)
# stacked = df2.stack()
# print(stacked)
# print(stacked.unstack())
# print(stacked.unstack(1))
# print(stacked.unstack(0))

# df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
#                    'B': ['A', 'B', 'C'] * 4,
#                    'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
#                    'D': np.random.randn(12),
#                    'E': np.random.randn(12)})
# print(df)
# print(pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C']))

# rng = pd.date_range('8/3/2018', periods=12, freq='T')
# print(len(rng))
# ts = pd.Series(np.random.randint(0, 10, len(rng)), index=rng)
# print(ts)
# print('---')
# print(ts.resample('5T', closed='right').sum())

# rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
# ts = pd.Series(np.random.randn(len(rng)), rng)
# print(ts)
# ts_utc = ts.tz_localize('UTC')
# print(ts_utc)
# print(ts_utc.tz_convert('US/Eastern'))

# rng = pd.date_range('1/1/2012', periods=5, freq='M')
# ts = pd.Series(np.random.randn(len(rng)), index=rng)
# print(ts)
# ps = ts.to_period()
# print(ps)
# print(ps.to_timestamp())

# prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
# ts = pd.Series(np.random.randn(len(prng)), prng)
# ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9
# print(ts.head())

# df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6], "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']})
# print(df)
# df["grade"] = df["raw_grade"].astype("category")
# print(df["grade"])
# df["grade"].cat.categories = ["very good", "good", "very bad"]
# print(df["grade"])
# df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
# print(df["grade"])
# print(df.sort_values(by="grade"))
# print(df.groupby("grade").size())

# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
# ts = ts.cumsum()
# # print(ts)
# ts.plot()
# df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
# df = df.cumsum()
# plt.figure()
# df.plot()
# plt.legend(loc='best')
# # df.A.plot()  # 对A列作图，同理可对行做图
# # df.B.plot(secondary_y=True, style='g')  # 设置第二个y轴（右y轴）
# # # 图2
# # ax = df.plot(secondary_y=['A', 'B'])  # 定义column A B使用右Y轴。ax（axes）可以理解为子图，也可以理解成对黑板进行切分，每一个板块就是一个axes
# # #  ax = df.plot(secondary_y=['A', 'B'], mark_right=False)#上一行默认图列会显示（right）, mark_right=False即关闭显示
# # ax.set_ylabel('CD scale')
# # ax.right_ax.set_ylabel('AB scale')
# # ax.legend(loc='upper left')  # 设置图例的位置
# # ax.right_ax.legend(loc='upper right')
# # #     ax.legend(loc='1')
# # #     plt.legend(loc='2')zhem
# # # 展示
# plt.show()

# ts = pd.Series(np.random.randint(1, 5), index=pd.date_range('1/1/2000', periods=10))
# print(ts)
# ts = ts.cumsum()
# print(ts)
# ts.plot()
# df = pd.DataFrame(np.random.randn(10, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
# print(df)
# # df.to_csv('foo.csv')
# # df.to_hdf('foo.h5', 'df')
# df.to_excel('foo.xlsx', sheet_name='Sheet1')

# broken_df = pd.read_csv('comptagevelo2012.csv')
# # print(broken_df[:5])
# print(broken_df.columns)
# # broken_df['Berri1'].plot()
# broken_df.plot(figsize=(15, 10))
# plt.show()


complaints = pd.read_csv(r'C:\Users\ex_wanghan\Downloads\311_Service_Requests_for_2009.csv')
print(complaints)
print(complaints.columns)
print(complaints['Complaint Type'].value_counts())
complaint_counts = complaints['Complaint Type'].value_counts()
print(complaint_counts[:10])
complaint_counts[:10].plot(kind='bar')
plt.show()

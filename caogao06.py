import numpy as np

# 0-1之间 生成形状为3*2的二维数组，注意这里不是((2,3))
a = np.random.rand(3, 2)
# print(a)

# 1-10之间
a1 = np.random.uniform(1, 10, (2, 3))
# print(a1)

# 标准正态分布，正负都有，3行2列, 大多 -10 -- +10之间
a2 = np.random.randn(3, 2)
# 经常会用到的np.random.randn(size)所谓标准正态分布（μ=0,σ=1μ=0,σ=1），
# 对应于np.random.normal(loc=0, scale=1, size)。
print(a2)

# # 均值为loc=1，标准差为scale=3, scale越大越矮胖，scale越小，越瘦高
a3 = np.random.normal(1, 3)
# print(a3)

# 1-10之间
a4 = np.random.randint(1, 10, (2, 3), dtype=np.int64)
# print(a4)
# print(np.random.randint(2))
# low=2：生成1个[0,2)之间随机整数
# print(np.random.randint(2, size=5))
# low=2,size=5 ：生成5个[0,2)之间随机整数
# print(np.random.randint(2, 6, size=5))
# low=2,high=6,size=5：生成5个[2,6)之间随机整数
# print(np.random.randint(2, size=(2, 3)))
# low=2,size=(2,3)：生成一个2x3整数数组,取数范围：[0,2)随机整数
# print(np.random.randint(2, 6, (2, 3)))
# low=2,high=6,size=(2,3)：生成一个2*3整数数组,取值范围：[2,6)随机整数

# [0, 1)之间的均匀抽样，3行2列
a5 = np.random.random((3, 2))
print(a5)

# 和 np.random.random作用一样
a6 = np.random.random_sample((2, 3))
# print(a6)

# a7 = np.random.choice(a, size=None, replace=True, p=None)
# 若a为数组，则从a中选取元素；若a为单个int类型数，则选取range(a)中的数
# replace是bool类型，为True，则选取的元素会出现重复；反之不会出现重复
# p为数组，里面存放选到每个数的可能性，即概率

# 总结：随机数可以分为两大类，一类是浮点型的，常以np.random.uniform为
# 代表，np.random.rand,np.random.random和np.random.random_simple可以
# 看作是np.random.uniform的特例；另一类是整数型的，以np.random.randint为
# 代表，也有np.random.random_integers 但是后者将被前者取代

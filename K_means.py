from random import uniform
from math import sqrt
import matplotlib.pyplot as plt
#创建一个数据集。
#注意：本方法创建的数据集每次运行结果都不相同
m = 60 #数据个数
data = [[],[]] #[[存储 x 轴数据],[存储 y 轴数据]]
for i in range(m):
    if i < m/3: 
        data[0].append(uniform(1,5))#随机设定
        data[1].append(uniform(1,5))
    elif i < 2*m/3:
        data[0].append(uniform(6,10))
        data[1].append(uniform(1,5))
    else:
        data[0].append(uniform(3,8))
        data[1].append(uniform(5,10))
print(data)
#将创建的数据集画成散点图
plt.scatter(data[0],data[1])
plt.xlim(0,11)
plt.ylim(0,11)
plt.show()

#定义欧几里得距离
def distEuclid(x1,y1,x2,y2):
    d = sqrt((x1-x2)**2+(y1-y2)**2)
    return d

cent0 = [uniform(2,9),uniform(2,9)] #定义 K=3 个质心，随机赋值
cent1 = [uniform(2,9),uniform(2,9)] #[x,y]
cent2 = [uniform(2,9),uniform(2,9)]
mark = [] #标记列表
dist = [[],[],[]]#各质心到所有点的距离列表
#核心
for n in range(50):
    #计算各质心到所有点的距离
    for i in range(m):
        dist[0].append(distEuclid(cent0[0],cent0[1],data[0][i],data[1][i]))
        dist[1].append(distEuclid(cent1[0],cent1[1],data[0][i],data[1][i]))
        dist[2].append(distEuclid(cent2[0],cent2[1],data[0][i],data[1][i]))
    #对数据进行整理
    sum0_x = sum0_y = sum1_x = sum1_y = sum2_x = sum2_y = 0
    number0 = number1 = number2 = 0
    for i in range(m):
        if dist[0][i]<dist[1][i] and dist[0][i]<dist[2][i]:
            mark.append(0)
            sum0_x += data[0][i]
            sum0_y += data[1][i]
            number0 += 1
        elif dist[1][i]<dist[0][i] and dist[1][i]<dist[2][i]:
            mark.append(1)
            sum1_x += data[0][i]
            sum1_y += data[1][i]
            number1 += 1
        elif dist[2][i]<dist[0][i] and dist[2][i]<dist[1][i]:
            mark.append(2)
            sum2_x += data[0][i]
            sum2_y += data[1][i]
            number2 += 1    
    #更新质心
    cent0 = [sum0_x/number0,sum0_y/number0]
    cent1 = [sum1_x/number1,sum1_y/number1]
    cent2 = [sum2_x/number2,sum2_y/number2]

#画图
for i in range(m):
    if mark[i] == 0:
        plt.scatter(data[0][i],data[1][i],color='red')
    if mark[i] == 1:
        plt.scatter(data[0][i],data[1][i],color='blue')
    if mark[i] == 2:
        plt.scatter(data[0][i],data[1][i],color='green')     
plt.scatter(cent0[0],cent0[1],marker='*',color='red')
plt.scatter(cent1[0],cent1[1],marker='*',color='blue')
plt.scatter(cent2[0],cent2[1],marker='*',color='green')
plt.xlim(0,11)
plt.ylim(0,11)
plt.show()

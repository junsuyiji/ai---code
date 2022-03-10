import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
df = pd.read_csv("boston.csv")
df = np.array(df.values,ndmin=2)
x_data = df[:,:12]
#归一化
for i in range(12):
    x_data[:,i] = (x_data[:,i]-x_data[:,i].min())/(x_data[:,i].max()-x_data[:,i].min())
y_data = df[:,12]
#将后10个作为测试集，不参加训练
test_x = x_data[-10:]
test_y = y_data[-10:]
#初始化参数
w = np.random.normal(0.0,1.0,(1,12))
b = 0.0
#设置训练轮次
train_epochs = 200
learing_rate = 0.001
loss_=[]
for count in range(train_epochs):
    loss=[]
    for i in range(len(x_data)):
        re = w.dot(x_data[i])+b
        err = y_data[i]-re
        w +=learing_rate*err*x_data[i]
        b +=learing_rate*err
        #记录误差
        loss.append(abs(err))
    loss_.append(sum(loss)/len(loss))
    #print(sum(loss)/len(loss))
    #随机打乱训练集中的样本，防止模型出现结果和输入的位置有关的情况
    x_data,y_data = shuffle(x_data,y_data)
#打印误差的变化情况
plt.plot(loss_)
#简单的评估，看看实际值和预测值之间的误差
for i in range(10):
    print("true:\t{}".format(test_y[i]),end="\t")
    pre = np.dot(w,test_x[i])+b
    print("guess:\t{}".format(pre))
plt.show()

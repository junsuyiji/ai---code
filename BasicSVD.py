
import random
import math
import numpy as np

class SVD(object):

    def __init__(self, rating_data, F, alpha=0.1, lmbd=0.1, max_iter=1000):
        """
        :param rating_data: rating_data是[(user,[(item,rate)]]类型
        :param F: 隐因子个数  这里设置的是2
        :param alpha: 学习率
        :param lmbd: 正则化
        :param max_iter:最大迭代次数
        """
        self.F = F  #隐因子个数
        self.P = dict()  # R=PQ^T，代码中的Q相当于博客中Q的转置 创建空的P的矩阵
        self.Q = dict()  #  创建空的Q矩阵  dict() 函数用于创建一个字典。
        self.alpha = alpha #学习率
        self.lmbd = lmbd   #正则化  正则化 (Regularization) 是机器学习中对原始损失函数引入额外信息，以便防止过拟合和提高模型泛化性能的一类方法的统称
        self.max_iter = max_iter #迭代次数
        self.rating_data = rating_data #读入的数据

        '''随机初始化矩阵P和Q'''
        # user 表示A,B,C rates表示
        for user, rates in self.rating_data:
            self.P[user] = [random.random() / math.sqrt(self.F)   #
                            for x in range(self.F)]
            
            #print(self.rating_data)
            #print(rates)
            #print(self.P)
            #print(user)
            for item, _ in rates:
                if item not in self.Q:
                    self.Q[item] = [random.random() / math.sqrt(self.F)
                                    for x in range(self.F)]
        #print(self.Q) 
    def train(self):
            """
            随机梯度下降法训练参数P和Q
            :return: 
            """
           
            for step in range(self.max_iter): #遍历次数max_iter
                for user, rates in self.rating_data:
                    for item, rui in rates:
                        hat_rui = self.predict(user, item)  #预测得分
                        err_ui = rui - hat_rui  #计算误差
                        for f in range(self.F): #梯度下降更新
                            self.P[user][f] += self.alpha * (err_ui * self.Q[item][f] - self.lmbd * self.P[user][f])
                            self.Q[item][f] += self.alpha * (err_ui * self.P[user][f] - self.lmbd * self.Q[item][f])
                self.alpha *= 0.9  # 每次迭代步长要逐步缩小
    def predict(self, user, item):
                """
                :param user:
                :param item:
                :return:
                预测用户user对物品item的评分
                """
                return sum(self.P[user][f] * self.Q[item][f] for f in range(self.F))

if __name__ == '__main__':
    '''用户有A B C，物品有a b c d'''
    rating_data = list()  #定义列表
    rate_A = [('a', 2.0), ('b', 1.0)]
    rating_data.append(('A', rate_A))  #在A的列表末尾添加新的对象
    rate_B = [('b', 1.0), ('c', 1.0)]
    rating_data.append(('B', rate_B))
    rate_C = [('c', 1.0), ('d', 1.0)]
    rating_data.append(('C', rate_C))
    #print(len(rating_data))
    #print(rating_data)
    svd = SVD(rating_data, 2) #2 表示隐因子个数
    svd.train()
    for item in ['a', 'b', 'c', 'd']:
        print(item, svd.predict('A', item)) # 计算用户A对各个物品的喜好程度
        
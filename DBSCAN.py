from numpy import *
from matplotlib import pyplot as plt
import math
import random


def loadData(fileName):
    dataSet = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split(' ')
        dataSet.append([float(lineArr[0]), float(lineArr[1])])
    return dataSet


def distance(sample1, sample2):
    return math.sqrt((sample1[0, 0] - sample2[0, 0]) ** 2 + (sample1[0, 1] - sample2[0, 1]) ** 2)


def neighbor(sample, dataSet, epsilon):
    m_neighor = []
    for data in dataSet:
        if distance(mat(sample), mat(data)) <= epsilon:
            m_neighor.append(data)
    return m_neighor


def dbscan(dataSet, epsilon, MinPts):
    core = []
    C = []
    for sample in dataSet:
        m_neighbor = neighbor(sample, dataSet, epsilon)
        if (mat(m_neighbor).shape[0] >= MinPts):
            core.append(sample)
    # 初始化聚类的个数
    k = 0
    # 初始化未访问过的样本集合
    F = []
    for s in dataSet:
        F.append(s)
    while len(core) != 0:
        F_Old = []
        for sample in F:
            F_Old.append(sample)
        i = random.randint(0, len(core) - 1)
        o = core[i]
        Q = []
        Q.append(o)
        F.remove(o)
        while len(Q) != 0:
            q = Q.pop(0)
            m_neighbor = neighbor(q, dataSet, epsilon)
            if len(m_neighbor) >= MinPts:
                # deta=list(set(m_neighbor).intersection(set(F)))
                deta = [val for val in m_neighbor if val in F]
                for sample in deta:
                    Q.append(sample)
                for sample in deta:
                    F.remove(sample)
        k += 1
        C_k = F_Old
        for sample in F:
            C_k.remove(sample)
        print(len(C_k))
        C.append(C_k)
        for sample in C_k:
            if sample in core:
                core.remove(sample)

    return C


if __name__ == '__main__':
    dataSet = loadData('watermelon4.txt')
    core = dbscan(dataSet, 0.11, 5)

    mark = ['og', '+b', 'sr', 'db','<r','or','ob']
    i = 0
    #j = 0
    for cluster in core:
        for sample in cluster:
            print(sample)
            plt.plot(sample[0],sample[1],mark[i])
            #j += 1
        i+=1
    plt.show()
    #print(j)
    print(len(dataSet))

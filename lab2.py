# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 17:11:24 2022

@author: User
"""

import matplotlib.pyplot as plt
from math import pow, sqrt
import numpy as np
fileName1 = input('Введіть назву файлу ')
def SortOfArray(data):
    for index in range(0, len(data)):
        min = index
        for comp in range(index + 1, len(data)):
            if data[comp] < data[min]:
                min = comp
        if min != index:
            data[index], data[min] = data[min], data[index]
    return data
def GetData(fileName):
    f = open(fileName, 'r')
    s = f.readline()
    n = int(s)
    arr=[]
    for line in f:
        data = line.split(' ')
        for s in data:
            if s != '':
                arr = arr+[int(s)]
    print(arr)
    print(SortOfArray(arr))
    return SortOfArray(arr)
n=GetData(fileName1)
outputFile='output_'+str(len(n))+'.txt'
def Quartiles():
    q1=0.25*(len(n)+1)
    q1=int(q1)
    q3=0.75*(len(n)+1)
    q3=int(q3)
    print("Нижній квартиль","(",q1,")", n[q1])
    print("Верхній квартиль","(",q3,")", n[q3])    
    p90=0.9*(len(n)+1)
    p90=int(p90)-1
    print("Пересентиль(90): ","(",p90,")", n[p90])
    with open(outputFile,"a") as f:
        f.write("Нижній квартиль"+"("+str(q1)+")"+str(n[q1])+"\n")
        f.write("Верхній квартиль"+"("+str(q3)+")"+str(n[q3])+"\n")
        f.write("Пересентиль(90): "+"("+str(p90)+")"+str(n[p90])+"\n")
def Deviations():
    sum=int(0)
    for i in range(0,len(n)):
        sum=sum+n[i]
    avrg=sum/len(n)
    sum=int(0)
    for i in range(0,len(n)):
        sum=sum+abs(n[i]-avrg)
    print("Середнє відхилення: ", round(sum/len(n),2))
    with open(outputFile,"a") as f:
        f.write("Середнє відхилення: "+str(round(sum/len(n),2))+"\n")
    sum=int(0)
    for i in range(0,len(n)):
        sum=sum+pow(n[i]-avrg,2)
    print("Стандартне середнє відхилення: ", round(sqrt(sum/(len(n)-1)),2))
    with open(outputFile,"a") as f:
        f.write("Стандартне середнє відхилення: "+str(round(sqrt(sum/(len(n)-1)),2))+"\n")
def BetterMarks():
    sum=int(0)
    for i in range(0,len(n)):
        sum=sum+n[i]
    avrg=sum/len(n)
    l=np.array([[avrg,1],[100,1]])
    r=np.array([95,100])
    res=np.linalg.solve(l,r)
    res1=[]
    for i in range(0,len(n)):
        res1.append(res[0]*n[i]+res[1])
        res1[i]=int(res1[i])
    print(str(res1))
    with open(outputFile,"a") as f:
        f.write(str(res1)+", ")
def StemAndLeaf():
    with open(outputFile, "a") as f:
        f.write('\n')
        if (n[0] < 100):
            c = int(str(n[0])[0])
            f.write('\n' + str(c) + ' | ')
        else:
            c = 10
            f.write('\n' + '10 | ')
        for i in range(0, len(n)):
            if (n[i] < 100):
                c1 = int(str(n[i])[0])
            else:
                c1 = 10
            if (c1 != c):
                f.write('\n' + str(c1) + ' | ')
                c = c1
            if (len(str(n[i])) == 2):
                f.write(str(n[i])[1] + ' ')
            else:
                f.write('0 ')
plt.boxplot(n)
plt.savefig('output_plot_'+str(len(n))+'.png')
Quartiles()
Deviations()
BetterMarks()
StemAndLeaf()